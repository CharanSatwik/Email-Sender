# 1.Enable two step verification for the email from whivh you want ton send.
# 2.Then, go to app passwords and generate a new password.
# 3.Enter the email from which you want to send in email_sender.
# 4.Enter the generated password in email_password.
# 5.Enter the email receiver in email_receiver.
# 6.Enter the subject and body of your choice.

from email.message import EmailMessage
import ssl
import smtplib
email_sender = ""
email_password = ""
email_receiver = ""

subject = "Email Sender using Python."
body = """
This is an email sender using python.
"""
em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["Subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
