from email.message import EmailMessage
from dotenv import load_dotenv
import os
import sys
import ssl
import smtplib

# Load variables from .env file
load_dotenv()

email_sender = "dihfahsihm@gmail.com"
email_password = os.getenv('PASSWORD')
email_receiver = input("Enter Receiver Email: ")

subject = "Testing the module"
body="""It is cool to send emails"""

em=EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] =subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
    print("Email was sent successfully")
    
