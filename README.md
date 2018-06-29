#IntegriHotline (267 485 5049)
One phone number to automatically forward any caller to the designated team member that is on call at any time.

##Directions for testing development setup
In a new terminal window run 
'''
ngrok http 5000
'''
Then, go to your Twilio account, click the phone icon, then manage numbers, thenclick on the given free trial phone number, and paste the link shown by the ngrok command with an extra '/answer' that tells twilio to refer to the answer function in our code to handle the call. 
'''
'''
Then, go to the main directory holding these files and run 
'''
source bin/activate
python answer_phone.py
'''
and a Flask server will be set up and the number is ready to recieve our calls. 

