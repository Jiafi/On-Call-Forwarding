# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC39f2976bb7fda1d0d6a3e727e41b6fb4"
auth_token = "40fccb6cbd172b25f0fe0d57632e06a0"
client = Client(account_sid, auth_token)

call = client.calls.create(
    to="+12154605160",
    from_="+12674855049",
    url="http://demo.twilio.com/docs/voice.xml"
)

print(call.sid)
