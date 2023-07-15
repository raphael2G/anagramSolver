# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client('AC7fb59d6b8870ffd9bc1b63183aa5ae12', '569b58f9d860cbf1fec597b34bc0123e')

def sendText(text):
    message = client.messages \
        .create(
            body=text,
            from_='+18778923157',
            to   ='+14125001001'
        )

    print(message.sid)
