# fire-and-weapon-detection
This is the working of weapon and fire detection and alerting systems using ML. We have developed a model that detects the fire and weapon using the live feed from the webcam, after detecting the weapon or fire we have integrated the code with Twilio API and SMTP API they both are used to send SMS and EMAIL notifications respectively. The API will automatically send the code to the respected authority in charge nearer to that incident. For example if it is an fire accident then the SMS and email will be send to the fire and safety department.  We have trained a model called YOLO V3 that be trained with more than 6000+ images and videos of fire and weapons for more accuracy. We have used open CV and numpy library to make it more efficient. We are able to attain very high accuracy only because of this YOLO V3 model which makes the detection of fire or weapon within few seconds. This is a real-time problem statement that can be done in all public places with just CCTV camera functioning. This project can avoid many accidents and incidents that can be avoided and also many lives can be saved from threats



# Problem Statement:

The increasing occurrences of fire accidents and security threats involving weapons in public places pose significant risks to the safety and security of individuals. Traditional surveillance methods are often insufficient to detect such incidents in real-time, leading to delays in response and potential harm to individuals and property. There is a pressing need for an efficient and reliable system that can accurately detect fires and weapons in real-time using live camera feeds and promptly alert the relevant authorities to mitigate the risks and ensure public safety.

# Solution: 
Our Fire and Weapon Detection System leverages YOLO V3 ML model, trained on a vast dataset of over 6000 images and videos, for real-time object detection. Integrated with CCTV feeds, OpenCV, and numpy, it swiftly identifies fires and weapons. Upon detection, Twilio API and SMTP API instantly alert relevant authorities via SMS and email, ensuring prompt response. This scalable system offers comprehensive monitoring in public spaces, from airports to schools, preventing accidents and threats. By providing proactive surveillance, it enhances public safety, potentially saving lives and safeguarding property, establishing a robust defense against potential risks.


 # Technical Implementation:

1.Machine Learning Model: 
            YOLOv3 utilized for real-time object detection, trained on a dataset of 6000+ images/videos of fires and weapons.
2.Image Processing: 
            OpenCV employed for capturing video frames, feature extraction, and applying object detection algorithms.
3.Communication APIs:
           Twilio API integrated for SMS notifications; SMTP API used for email notifications with app-specific password authentication.
4.Script Configuration:
          chosen.py script configured with parameters like phone numbers, email addresses, and paths to pre-trained weights.
5.Execution:
          Script activates webcam for real-time detection; upon detection, sends SMS alerts via Twilio and emails with detected object images via SMTP.
6.Feedback Mechanism: 
         Voice feedback and console messages provide updates on detection and notification statuses

# Technical Stack:

*Python
*OpenCV
*YOLOv3
*Twilio API
*SMTP API

# How to run
STEP 1 
Install the required library functions

STEP 2 
create an account in Twilio API, copy the SSID and API token also copy the default from the phone number 

STEP 3 
https://drive.google.com/file/d/1IO4t9E-4AcNo61dayzzfyvW1AfV-1MC8/view?usp=sharing
https://drive.google.com/file/d/1TI2VhT3FqCQYoCARFcAu03c-5g7genaU/view?usp=sharing

From the provided link please download the WEIGHTS files.

STEP 4
In the repo, open the "chosen.py"

STEP 5
Replace the from phone number with the default phone number from the Twilio API and replace the to phone number with the respective phone number that is to receive the SMS alert (lines 62 and 63).

STEP 6 
Then in lines 43,44,45 change the from email ID to your custom email and generate the app lock for the mail ID(you can generate the app lock for your account in your Google account), then replace the received mail ID with the respective mail ID that is to be received.

STEP 7
In line 22 load the downloaded WEIGHT files and replace them (WEIGHT files link in above step-3)

STEP 8
If you wish to detect the weapon or the fire from the already existing image or video(that should contain a weapon or fire) then in line 10 change the default value to "False" and in line 11 change it to "True" and then copy the path of the file and replace it in the 13th line of the "chosen.py" file.

STEP 9
Run the code by pressing "ctrl + f5"

STEP 10
If you wish to detect the weapon or fire from the webcam then in line 11 change it to "False" and in line 10 change it to "True"

STEP 11 
Now run the code by pressing "ctrl + f5", you will be able to see a white color light near the laptop camera and a pop-up window of the camera.

STEP 12 
In the terminal, you can find the output as "SMS sent successfully" and a voice that can be heard states that "weapon" or "fire detected".

STEP 13
You can see the SMS on the receiver's phone and the email contains the images of the fire that is been detected.

These are the steps to run the code.

# Future perpespective 
In the foreseeable future, the Fire and Weapon Detection System holds tremendous potential for revolutionizing public safety and security across diverse environments. As it evolves, the system can seamlessly integrate with smart city infrastructures, extending its surveillance capabilities to streets, parks, and transportation hubs. By leveraging real-time monitoring and analytics, authorities can proactively manage risks and allocate resources effectively. Collaboration among security agencies and integration with IoT devices can further enhance its reach and effectiveness. However, ensuring privacy protection and ethical use will be crucial, necessitating stringent regulations and public education efforts. As the system gains global adoption, standardization efforts and continuous innovation will drive its evolution, ultimately fostering safer communities and mitigating potential threats to lives and property.

# Declartion 
We confirm that the project showcased here was either developed entirely during the hackathon or underwent significant updates within the hackathon timeframe. We understand that if any plagiarism from online sources is detected, our project will be disqualified, and our participation in the hackathon will be revoked.


