from flask import (
   Flask,
   Response,
   redirect,
   render_template,
   request,
   url_for,
)
from twilio.twiml.voice_response import VoiceResponse
from on_call import get_oncall, get_schedules
from twilio.twiml.voice_response import VoiceResponse, Gather


schedules = get_schedules()
app = Flask(__name__)
@app.route("/answer", methods = ['GET','POST'])
def get_team():
    command = ''
    for i in range(len(schedules)):
        command += 'Press %d for %s.   ' %(i+1,schedules[i])
   # command = "Press 1 for S.R.E.. Press 2 for Nick"
    response = VoiceResponse()
    gather = Gather(
            num_digits=1,
            action='/forward',
            method='POST'
            )
    gather.say(command)
    response.append(gather)
    return (str(response), 200)

@app.route('/forward', methods=['GET','POST'])
def hello():
    """ REspond to incoming phone calls with a brief message. """
    team = int(request.values.get('Digits', None))
    resp = VoiceResponse()
    
    # Read a message aloud to the caller
    resp.say("You pressed the number for  %s. We will forward you now." % (schedules[team-1]), voice = 'bob') 
    resp.dial(get_oncall(schedules[team-1]))
    return str(resp)
'''
Nick! Put the below code inside your /answer function call.
'''
if __name__ == "__main__":
    app.run(debug=True)

#@app.route("say_input", methods = ['GET', 'POST'])
#3def say_input():
    
    
