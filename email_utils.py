import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import Config

def send_email(db_name, status, app_id):
    # Creates the message
    msg = MIMEMultipart()
    msg['From'] = Config.EMAIL_USER
    msg['To'] = Config.EMAIL_RECIPIENT
    msg['Subject'] = f"Database Status Notification for {db_name}"

    # Creates the HTML body
    status_color = "green" if status == "online" else "red"
    body = f"""
    <html>
    <body>
        <p>Application ID: {app_id}</p>
        <p>Database Name: {db_name}</p>
        <p>Status: <span style="color:{status_color};">{status}</span></p>
    </body>
    </html>
    """
    msg.attach(MIMEText(body, 'html'))

    # Sends the email
    try:
        with smtplib.SMTP(Config.EMAIL_HOST, Config.EMAIL_PORT) as server:
            server.starttls()
            server.login(Config.EMAIL_USER, Config.EMAIL_PASSWORD)
            server.sendmail(Config.EMAIL_USER, Config.EMAIL_RECIPIENT, msg.as_string())
        print(f"Email sent to {Config.EMAIL_RECIPIENT} regarding {db_name} status.")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")
