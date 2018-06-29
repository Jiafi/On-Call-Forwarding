# IntegriHotline (267 485 5049)
One phone number to automatically forward any caller to the designated team member that is on call at any time.

## Directions for testing development setup
In a new terminal window run 
```
ngrok http 5000 
```
Then, go to your Twilio account, click the phone icon, then manage numbers, thenclick on the given free trial phone number, and paste the link shown by the ngrok command with an extra '/answer' that tells twilio to refer to the answer function in our code to handle the call. 
Then, go to the main directory holding these files and run 
```
source bin/activate
python answer_phone.py
```
And a Flask server will be set up and the number is ready to recieve our calls. 

## Pre-requisites 
This project is written in Python 2.7.15, uses Flask as a server and ngrok as a reverse proxy tunnel for easy use in a testing environment. 
### Install 
The project was inspired by [This link](https://www.twilio.com/docs/voice/quickstart/python). </br>
These directions were followed to set up an account and phone number with Twilio and to download ngrok. (I found [This link](https://gist.github.com/wosephjeber/aa174fb851dfe87e644e) particularly helpful to install ngrok and for setting up the ngrok command. 
</br>
The project also pulls data from pager duty to get the schedules of team members who are on call. 
