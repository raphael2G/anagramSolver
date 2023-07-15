# Download the helper library from https://www.twilio.com/docs/python/install

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure


from twilio.rest import Client

account_sid = 'AC7fb59d6b8870ffd9bc1b63183aa5ae12'
auth_token = 'c6c74757fa9216588ed09da055f18d53'
client = Client(account_sid, auth_token)

def sendText(text):
    message = client.messages.create(
        body=text,
        from_='+18778923157',
        to='+14125001001'
    )
