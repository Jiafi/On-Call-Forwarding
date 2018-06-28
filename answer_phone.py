from flask import Flask, url_for
from twilio.twiml.voice_response import VoiceResponse
from on_call import get_oncall

app = Flask(__name__)

@app.route("/answer", methods = ['GET','POST'])
def hello():
    """ REspond to incoming phone calls with a brief message. """
    resp = VoiceResponse()

    # Read a message aloud to the caller
    resp.say("Thank you for calling! Have a great day.", voice = 'bob')
    
    resp.dial(get_oncall())
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

#@app.route("say_input", methods = ['GET', 'POST'])
#3def say_input():
    
    
