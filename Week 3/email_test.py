import os.path
import mimetypes
import smtplib
import getpass
from email.message import EmailMessage


def send_mail():
    pass


if __name__ == '__main__':
    sender = "bsprashanth1992@gmail.com"
    recipient = "bsprashanth92@gmail.com"
    # message = EmailMessage()
    # message["From"] = sender
    # message["To"] = recipient
    # message["Subject"] = "Greetings from {} to {}!".format(sender, recipient)
    # body = """Hey there!
    # ...
    # ... I'm learning to send emails using Python!"""
    # message.set_content(body)
    # attachment_path = "test/img.jpeg"
    # attachment_filename = os.path.basename(attachment_path)
    # mimetype, _ = mimetypes.guess_type(attachment_filename)
    # mime_type, mime_subtype = mimetype.split('/')
    # print(mime_type, mime_subtype)
    #
    # with open(attachment_path, 'rb') as ap:
    #     message.add_attachment(ap.read(), maintype=mime_type, subtype=mime_subtype, filename=os.path.basename(attachment_path))
    # print(message)

    # mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
    # mail_server.set_debuglevel(1)
    # mail_pass = getpass.getpass('Password? ')
    # mail_pass = "Teenqueen123"

    # mail_server.login(sender, mail_pass)
    # mail_server.send_message(message)
    # mail_server.quit()