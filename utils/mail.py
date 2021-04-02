from flask_mail import Message
from config.config import MAIL_DEFAULT_SENDER


def send_email(mail, subject, recipients, html_body):
    msg = Message(subject, sender=MAIL_DEFAULT_SENDER, recipients=recipients)
    msg.html = html_body

    try:
        mail.send(msg)
    except ConnectionRefusedError:
        raise Exception("An error occurred while connecting to the mail server")
