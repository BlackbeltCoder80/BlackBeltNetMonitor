import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SUSPICIOUS_SITES = ["pornhub.com", "darkweb", "illegal-site.com"]

def send_alert(message):
    """ Send an alert via email """
    sender_email = "your_email@gmail.com"
    sender_password = "your_app_password"
    receiver_email = "your_email@gmail.com"

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = "🚨 Network Security Alert!"
    msg.attach(MIMEText(message, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print(f"📧 ALERT SENT: {message}")
    except Exception as e:
        print(f"❌ Alert Failed: {e}")

if __name__ == "__main__":
    send_alert("Test alert message")
