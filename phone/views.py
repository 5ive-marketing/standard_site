from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse

from five import settings
from twilio.rest import Client

from twilio.twiml.voice_response import Dial, VoiceResponse, Say


def voice():
    """Respond to incoming phone calls with a menu of options"""
    # Start our TwiML response
    resp = twiml.Response()

    # Start our <Gather> verb
    with resp.gather(numDigits=1, action='/gather') as gather:
        gather.play('http://5ivemarketing.com/static/phone/audio/Memo.mp3')

    # If the user doesn't select an option, redirect them into a loop
    resp.redirect('/voice')


def gather():
    """Processes results from the <Gather> prompt in /voice"""
    # Start our TwiML response
    resp = twiml.Response()

    # If Twilio's request to our app included already gathered digits,
    # process them
    if 'Digits' in request.values:
        # Get which digit the caller chose
        choice = request.values['Digits']
        if choice == '1':
            response.say(
                'Voicemail is currently unavailible, redirecting you to Mike Peterson')
            response.dial('+15033839340')
            responce.hangup()

        # michael clark
        if choice == '2':
            response.dial('+15036832405')
            response.say(
                'The call failed or the remote party hung up. Goodbye.')
            responce.hangup()
        # mike peterson
        elif choice == '3':
            response.dial('+15033839340')
            response.say(
                'The call failed or the remote party hung up. Goodbye.')
            responce.hangup()
        # events
        elif choice == '4':
            response.say(
                'We don\'t currently have any events scheduled. Please check back again soon.')
            responce.hangup()

        else:
            # If the caller didn't choose 1 or 2, apologize and ask them again
            resp.say("Sorry, I don't understand that choice.")

    # If the user didn't choose 1 or 2 (or anything), send them back to /voice
    resp.redirect('/voice')
