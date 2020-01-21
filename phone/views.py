from twilio.twiml.voice_response import VoiceResponse
from django_twilio.decorators import twilio_view
from django.core.mail import send_mail


@twilio_view
def voice(request):
    r = VoiceResponse()

    with r.gather(numDigits=1, action='choice') as gather:
        gather.play('http://5ivemarketing.com/static/phone/audio/Memo.mp3')

    return r


@twilio_view
def choices(request):
    """Processes results from the <Gather> prompt in /voice"""
    # Start our TwiML response
    r = VoiceResponse()

    # If Twilio's request to our app included already gathered digits,
    # process them
    if request.POST.get('Digits'):
        # Get which digit the caller chose
        choice = request.POST.get('Digits')

        if choice == '1':
            r.say(
                'Please leave a message after the tone.')
            r.record(timeout=20, playBeep=True)
            r.hangup()

        # michael clark
        elif choice == '2':
            r.dial('+15036832405')
            r.say(
                'The call failed or the remote party hung up. Goodbye.')
            r.hangup()
        # mike peterson
        elif choice == '3':
            r.dial('+15033839340')
            r.say(
                'The call failed or the remote party hung up. Goodbye.')
            r.hangup()
        # events
        elif choice == '4':
            r.say(
                'We don\'t currently have any events scheduled. Please check back again soon.')
            r.hangup()

        else:
            # If the caller didn't choose 1 or 2, apologize and ask them again
            r.say("Sorry, I don't understand that choice.")

    return r


@twilio_view
def mail(request):

    r = VoiceResponse()

    from_ = request.POST.get('request.POST.get('')')
    url = request.POST.get('RecordingUrl') + '.mp3'

    subject = 'New message from ' + from_
    message = 'New voice mail from: ' + from_
    message += ' play the message by clicking on the following URL: ' + url
    from_email = 'info@5ivemarketing.com'
    recipient_list = ['dominic.groshong@5ivemarketing.com']

    send_mail(subject, message, from_email,
              recipient_list, fail_silently=False)

    return r
