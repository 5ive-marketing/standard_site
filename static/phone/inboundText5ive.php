<?php
require_once 'vendor/autoload.php'; // Loads the library
use Twilio\Twiml;

$response = new Twiml;
$body = $_REQUEST['Body'];
$default = "Hello! Im the 5ive Marketing message bot. To contact a department respond with:";
$options = "info, sales, support";
$info = "Text or Call: Mike Peterson - 555.555.555";
$sales = "Text or Call: Michael Clark - 555.555.5555";
$support = "Text: Dominic Groshong - 555.555.5555";

if (strtolower($body) == 'info') {
  $response->message($info);
} else {
  $response->message($default);
  $response->message($options);
}
print $response;
