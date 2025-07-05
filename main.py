

import cv2
import face_recognition
import os
import numpy as np
from datetime import datetime
from send_email import send_email
# from send_whatsapp import send_whatsapp
from log_writer import log_intruder

# Paths
KNOWN_FACES_DIR = "known_faces"
UNKNOWN_FACES_DIR = "unknown_faces"
LOG_PATH = "logs/log.csv"

# Ensure required folders exist
os.makedirs(KNOWN_FACES_DIR, exist_ok=True)
os.makedirs(UNKNOWN_FACES_DIR, exist_ok=True)
os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

# Load known faces
known_encodings = []
known_names = []

print("[INFO] Loading known faces...")

for filename in os.listdir(KNOWN_FACES_DIR):
    filepath = os.path.join(KNOWN_FACES_DIR, filename)
    try:
        image = face_recognition.load_image_file(filepath)
        encodings = face_recognition.face_encodings(image)
        if len(encodings) > 0:
            known_encodings.append(encodings[0])
            known_names.append(os.path.splitext(filename)[0])
        else:
            print(f"[WARNING] No face found in {filename}, skipping.")
    except Exception as e:
        print(f"[ERROR] Failed to load {filename}: {e}")

print(f"[INFO] Loaded {len(known_names)} known face(s).")

# Start webcam
video = cv2.VideoCapture(0)

if not video.isOpened():
    print("[ERROR] Could not open webcam.")
    exit()

print("[INFO] Security cam is running... Press 'q' to quit.")

while True:
    ret, frame = video.read()

    if not ret or frame is None:
        print("[WARNING] Skipping empty frame...")
        continue

    if len(frame.shape) != 3 or frame.shape[2] != 3:
        print("[WARNING] Unsupported frame format. Skipping...")
        continue

    try:
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    except Exception as e:
        print(f"[ERROR] Failed to convert frame to RGB: {e}")
        continue

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        name = "Unknown"

        if known_encodings:
            matches = face_recognition.compare_faces(known_encodings, face_encoding)
            if True in matches:
                match_index = matches.index(True)
                name = known_names[match_index]

        if name == "Unknown":
            now = datetime.now()
            timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"intruder_{timestamp}.jpg"
            filepath = os.path.join(UNKNOWN_FACES_DIR, filename)
            cv2.imwrite(filepath, frame)

            print(f"[ALERT] Intruder detected! Image saved as {filename}")

            # Send alert
            send_email(filepath, timestamp)
            # send_whatsapp(timestamp)

            # Log
            log_intruder(name, timestamp, filepath)

    # Optional display
    cv2.imshow("Smart Security Cam", frame)
    if cv2.waitKey(1) == ord("q"):
        break

video.release()
cv2.destroyAllWindows()

