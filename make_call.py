# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC39f2976bb7fda1d0d6a3e727e41b6fb4'
auth_token = '40fccb6cbd172b25f0fe0d57632e06a0'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='+12154605160',
                        from_='+12674855049'
                    )

print call.sid
