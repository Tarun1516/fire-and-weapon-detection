import cv2
import numpy as np 
import argparse
from twilio.rest import Client
import smtplib
from email.message import EmailMessage
import pyttsx3

parser = argparse.ArgumentParser()
parser.add_argument('--webcam', help="True/False", default=True)
parser.add_argument('--play_video', help="True/False", default=False)
parser.add_argument('--image', help="True/False", default=False)
parser.add_argument('--video_path', help="Path of video file", default="C:\\Users\\swamy\\OneDrive\\Desktop\\fire-and-gun-detection-master\\fire-and-gun-detection-master\\videos\\fire1.mp4")
parser.add_argument('--image_path', help="Path of image to detect objects", default="Images/bicycle.jpg")
parser.add_argument('--verbose', help="To print statements", default=True)
args = parser.parse_args()

# Initialize text-to-speech engine
engine = pyttsx3.init()

def load_yolo():
    net = cv2.dnn.readNet("C:\\Users\\swamy\\OneDrive\\Desktop\\fire-and-gun-detection-master\\fire-and-gun-detection-master\\yolov3.weights", "C:\\Users\\swamy\\OneDrive\\Desktop\\fire-and-gun-detection-master\\fire-and-gun-detection-master\\yolov3.cfg")
    classes = []
    with open("C:\\Users\\swamy\\OneDrive\\Desktop\\fire-and-gun-detection-master\\fire-and-gun-detection-master\\obj.names", "r") as f:
        classes = [line.strip() for line in f.readlines()]

    layers_names = net.getLayerNames()
    unconnected_layers = net.getUnconnectedOutLayers()[::-1]
    output_layers = [layers_names[i - 1] for i in unconnected_layers]
    colors = np.random.uniform(0, 255, size=(len(classes), 3))
    
    return net, classes, colors, output_layers

def send_email(frame, message):
    msg = EmailMessage()
    msg.set_content(message)
    
    _, img_encoded = cv2.imencode('.jpg', frame)
    img_bytes = img_encoded.tobytes()
    
    msg.add_attachment(img_bytes, maintype="image", subtype="jpg")
    
    msg['subject'] = "Alert!"
    msg['to'] = "9921004713@Klu.ac.in"  # replace with the recipient's email
    msg['from'] = "99220040949@klu.ac.in"  # replace with your sender email
    password = "ifwd uent apdv qeix"  # replace with your email password

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(msg['from'], password)
    server.send_message(msg)
    server.quit()

def send_sms(message):
    account_sid = 'ACae7106ed4a1802c5b39b767e5f9b6e1b'
    auth_token = 'd1ce435301b687f32677c849119b14ee'
    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
        body=message,
        from_='+12092623136',  # replace with your Twilio phone number
        to='+918778738627'  # re7lace with the recipient's phone number
    )
    print("SMS sent successfully!")

def load_image(img_path):
    img = cv2.imread(img_path)
    img = cv2.resize(img, None, fx=0.4, fy=0.4)
    height, width, channels = img.shape
    return img, height, width

def detect_objects(img, net, outputLayers):
    blob = cv2.dnn.blobFromImage(img, scalefactor=0.00392, size=(320, 320), mean=(0, 0, 0), swapRB=True, crop=False)
    net.setInput(blob)
    outputs = net.forward(outputLayers)
    return blob, outputs

def get_box_dimensions(outputs, height, width):
    boxes = []
    confs = []
    class_ids = []
    for output in outputs:
        for detect in output:
            scores = detect[5:]
            class_id = np.argmax(scores)
            conf = scores[class_id]
            if conf > 0.6:
                center_x = int(detect[0] * width)
                center_y = int(detect[1] * height)
                w = int(detect[2] * width)
                h = int(detect[3] * height)
                x = int(center_x - w/2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confs.append(float(conf))
                class_ids.append(class_id)

    return boxes, confs, class_ids

def draw_labels(boxes, confs, colors, class_ids, classes, frame):
    detected_classes = set()
    for i in range(len(boxes)):
        x, y, w, h = boxes[i]
        label = str(classes[class_ids[i]])
        confidence = confs[i]
        color = colors[class_ids[i] % len(colors)]
        cv2.rectangle(frame, (round(x), round(y)), (round(x + w), round(y + h)), color, 2)
        cv2.putText(frame, f"{label} {confidence:.2f}", (round(x), round(y) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        
        if class_ids[i] in [0, 2]:  # Check for weapon
            detected_classes.add("Weapon")
            # Draw bounding box around weapon
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, 'Weapon', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        elif class_ids[i] == 1:  # Check for fire
            detected_classes.add("Fire")
            # Draw bounding box around fire
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, 'Fire', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    
    if detected_classes:
        if "Fire" in detected_classes and "Weapon" in detected_classes:
            msg1 = "Fire and weapon detected"
            send_email(frame,msg1 )
            send_sms(msg1)
            # Speak the response
            engine.say(msg1)
            engine.runAndWait()
        elif "Fire" in detected_classes:
            msg2 = "Fire detected"
            send_email(frame, msg2)
            send_sms(msg2)
            # Speak the response
            engine.say(msg2)
            engine.runAndWait()
        elif "Weapon" in detected_classes:
            msg3 = "Weapon detected"
            send_email(frame,msg3 )
            send_sms(msg3)
            # Speak the response
            engine.say(msg3)
            engine.runAndWait()

    cv2.imshow("Object Detection", frame)

def webcam_detect():
    model, classes, colors, output_layers = load_yolo()
    cap = cv2.VideoCapture(0)
    while True:
        _, frame = cap.read()
        height, width, _ = frame.shape
        blob, outputs = detect_objects(frame, model, output_layers)
        boxes, confs, class_ids = get_box_dimensions(outputs, height, width)
        draw_labels(boxes, confs, colors, class_ids, classes, frame)
        key = cv2.waitKey(1)
        if key == 27:
            break
    cap.release()

def start_video(video_path):
    model, classes, colors, output_layers = load_yolo()
    cap = cv2.VideoCapture(video_path)
    while True:
        _, frame = cap.read()
        height, width, _ = frame.shape
        blob, outputs = detect_objects(frame, model, output_layers)
        boxes, confs, class_ids = get_box_dimensions(outputs, height, width)
        draw_labels(boxes, confs, colors, class_ids, classes, frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    cap.release()

def image_detect(img_path): 
    model, classes, colors, output_layers = load_yolo()
    image, height, width = load_image(img_path)
    blob, outputs = detect_objects(image, model, output_layers)
    boxes, confs, class_ids = get_box_dimensions(outputs, height, width)
    draw_labels(boxes, confs, colors, class_ids, classes, image)
    while True:
        key = cv2.waitKey(1)
        if key == 27:
            break

if __name__ == '__main__':
    webcam = args.webcam
    video_play = args.play_video
    image = args.image
    if webcam:
        if args.verbose:
            print('---- Starting Web Cam object detection ----')
        webcam_detect()
    if video_play:
        video_path = args.video_path
        if args.verbose:
            print('Opening '+video_path+" .... ")
        start_video(video_path)
    if image:
        image_path = args.image_path
        if args.verbose:
            print("Opening "+image_path+" .... ")
        image_detect(image_path)
    cv2.destroyAllWindows()
