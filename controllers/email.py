import smtplib, ssl
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_mail(receiver):
    sender_email = os.getenv('SENDER_EMAIL')
    gmail_password = os.getenv('GMAIL_PASSWORD')

    message = MIMEMultipart("alternative")
    message["Subject"] = "You're invited in our company - please fill the form"
    message["From"] = sender_email
    message["To"] = receiver

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(sender_email, gmail_password)

        text = """\
        """
        html = """\
        <html>
          <body>
                <h1> Hello, </h1>
                <h2>You're invited to fill the form to complete your user creation in our database</h2>
                <a href="{}/{}">Form to fill</a>
          </body>
        </html>
        """.format(os.getenv('LOCAL_SERVER_HOST'), receiver)

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, gmail_password)
            server.sendmail(
                sender_email, receiver, message.as_string()
            )

    except:
        print
        'Something went wrong...'

    return 'hello'
