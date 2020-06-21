from email.mime.text import MIMEText
import smtplib

def send_email(email, word, definition):
    from_email="nksonlinedictionary@gmail.com"
    from_password="python@123"
    to_email=email

    subject="Definition of the word"
    message="Hey there ,The word you have requested is <strong>%s</strong>.Definition: <strong>%s</strong>. Thank you for contacting us." %(word, definition)

    msg=MIMEText(message, 'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
