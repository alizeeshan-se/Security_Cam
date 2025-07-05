import smtplib
from email.message import EmailMessage
import os

EMAIL_ADDRESS = "shani030745@gmail.com"         # write your email address here of which you will create the app password
EMAIL_PASSWORD = "write your app password here"  # Use App Password, not real password

def send_email(image_path, timestamp):
    msg = EmailMessage()
    msg["Subject"] = f"Intruder Alert! [{timestamp}]"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = "codingalizeeshanse@gmail.com" # write your email address to which the alert will be sent
    msg.set_content(f"Hey Zeeshan! an unknown person was detected at {timestamp}.\nSee the attached photo.")

    with open(image_path, "rb") as f:
        file_data = f.read()
        file_name = os.path.basename(image_path)
        msg.add_attachment(file_data, maintype="image", subtype="jpeg", filename=file_name)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

    print("[EMAIL] Intruder alert email sent.")
