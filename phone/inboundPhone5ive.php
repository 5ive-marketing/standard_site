<?php

require_once 'vendor/autoload.php';
use Twilio\TwiML\VoiceResponse;

$response = new VoiceResponse();

// If the user entered digits, process their request
if (array_key_exists('Digits', $_POST)) {
  switch ($_POST['Digits']) {
    // Record a voicemail.
    case 1:
      $response->say('Please leave a message after the tone.');
      $response->record(['action' => 'voicemail/mail.php']);
      $response->hangup();
      break;
    // Case 2 is for Michael Clark
    case 2:
      $response->dial('+15036832405');
      $response->say('The call failed or the remote party hung up. Goodbye.');
      $response->hangup();
      break;
    // Case 3 is for Mike Peterson
    case 3:
      $response->dial('+15033839340');
      $response->say('The call failed or the remote party hung up. Goodbye.');
      $response->hangup();
      break;
    // Case 4 is for our events
    case 4:
      $response->say('We don\'t currently have any events scheduled. Please check back again soon.');
    default:
      $response->say('Sorry, I don\'t understand that choice.');
  }
} else {
  // If no input was sent, use the <Gather> verb to collect user input
  $gather = $response->gather(array('numDigits' => 1));
  // use the <Say> verb to request input from the user
  $gather->play('http://5ivemarketing.com/phone/audio/Memo.mp3');

  // If the user doesn't enter input, loop
  $response->redirect('/voice');
}

echo $response;
