import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os

def send_email_report(sender_email, sender_password, recipient_email, report_path):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = "Leadrat Automation Test Report"

    body = "Hi,\n\nPlease find the attached HTML test report.\n\nRegards,\nAutomation System"
    msg.attach(MIMEText(body, 'plain'))

    with open(report_path, "rb") as file:
        part = MIMEApplication(file.read(), Name=os.path.basename(report_path))
        part['Content-Disposition'] = f'attachment; filename="{os.path.basename(report_path)}"'
        msg.attach(part)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        print("✅ Report sent successfully!")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
    finally:
        server.quit()


# ---------- Replace the below values ----------
sender_email = "sudeshmahato000@gmail.com"
sender_password = "ixwvhnpjykprpfxe"
recipient_email = "jayakumar.k@leadrat.com"
report_path = r"/Leadrat_FrameWork/reports/Report.html"  # Full path to your HTML report

send_email_report(sender_email, sender_password, recipient_email, report_path)
