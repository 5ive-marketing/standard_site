<?php

/**
* This section ensures that Twilio gets a response.
*/
header('Content-type: text/xml');
echo '<?xml version="1.0" encoding="UTF-8"?>';

/**
* This section actually sends the email.
*/

$url = $_REQUEST['RecordingUrl'] . '.mp3';

/* Your email address. */
$to = "mike.peterson@5ivemarketing.com"; // accounts@5ivemarketing.com
$subject = "New Voicemail from {$_REQUEST['From']}";
$message = "You have received a message from {$_REQUEST['From']}.";
$message = "Play the message by clicking on the following URL: " . $url;
// $message .= "To listen to this message, please visit this URL: ";
$headers = "From: Twilio"; // Who should it come from?
mail($to, $subject, $message, $headers);
