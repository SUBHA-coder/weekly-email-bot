import os
import smtplib
from email.mime.text import MIMEText

def send_email():
    sender = os.environ['EMAIL']
    password = os.environ['PASSWORD']
    recipients = ["recipient1@example.com", "recipient2@example.com"]

    subject = "Weekly Update"
    body = "Hello! This is your weekly automated email."

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = ", ".join(recipients)

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, recipients, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    send_email()
