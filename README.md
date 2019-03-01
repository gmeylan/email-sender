# email-sender

To run the project `pip install -r requirements.txt` then `python server.py`

You'll need also to run the LDAP server image with `docker run -p 389:389 -p 636:636 --name my-openldap-container --detach osixia/openldap:1.2.3`

There are several environment variable to set. You'll need a google smtp server.  [Here is how to have the informations]([https://www.[google](https://support.google.com/a/answer/176600).com](https://support.google.com/a/answer/176600)).

The env variables are

SENDER_EMAIL -> the gmail account
GMAIL_PASSWORD -> the password of the app to access the gmail smtp
LOCAL_SERVER_HOST -> where the server is running, for dev: http:localhost:5000
LDAP_SERVER_HOST -> the host of the LDAP server
