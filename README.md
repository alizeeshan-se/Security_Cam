# Smart Security Cam

**Smart Security Cam** is a 24/7 face-recognition-based security camera system built with Python. It detects, identifies, and logs all visitors — and instantly alerts the owner in case of unknown intruders.

---

## Overview

This project functions as a smart door or area monitoring system. The security camera:

- Continuously opens the live camera feed  
- Detects faces when a person appears  
- Matches the detected face against a set of known individuals (owner, friends, or relatives)  
- Sends an alert with a photo to the owner's email if the face is unknown  
- Logs all visitors (both known and unknown) into a `.csv` file, acting as a visitor database

---

## Features

- Real-time camera feed with face detection  
- Recognizes known faces using a pre-trained dataset  
- Sends email alerts with a captured image if an unknown person is detected  
- Maintains a detailed log file (`.csv`) of all visitors with date and time  
- Organized folder structure for storing known and unknown face images

---

## Tech Stack

- **Python**  
- **OpenCV** – for camera access and face detection  
- **face_recognition** – for face identification  
- **smtplib** – for sending email alerts  
- **pandas** – for logging data into a `.csv` file  
- **datetime** – for timestamping visitor entries

---

## How to Use

1. **Clone the repository**  
   ```bash
   git clone https://github.com/alizeeshan-se/Security_Cam.git

Add known face images
Place images of known individuals in the known/ folder with meaningful file names (e.g., father.jpg, friend.png).

Run the script

bash
Copy
Edit
python main.py
Email configuration
Make sure to provide correct sender and receiver email addresses and the app password in the email.py file.

Developed By
Zeeshan Ali

LinkedIn:
https://www.linkedin.com/in/zeeshan-ali-59142b324/

Portfolio:
https://alizeeshan-se.github.io/my_portfolio_website/

GitHub:
https://github.com/alizeeshan-se


