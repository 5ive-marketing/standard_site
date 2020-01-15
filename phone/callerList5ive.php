<?php
     // if the caller pressed anything but 1,2,3,4 send them back to the main menu
    $values = array("1","2","3","4");
/*
    if(!in_array($_REQUEST['Digits'], $values)) {
       header("Location: inboundPhone5ive.php");
       die;
    } elseif($_REQUEST['Digits'] == 1) {
       header("Location: voicemail/leave_a_message.php?exten=0000");
       die;
    }
*/

    // Build page headers
    header("content-type: text/xml");
    echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n";
?>

<?php
switch ($_REQUEST['Digits']) {

    case 1:
?>
	 	<!-- <Response>
        <Say>Thanks for calling, please leave a message.</Say>
        <Record action="voicemail/mail.php"/>
    </Response> -->
<?php
    // Case 2 is for Michael Clark
    case 2:
?>
        <Response>
          <Dial>+15036832405</Dial>
          <Say>The call failed or the remote party hung up. Goodbye.</Say>
        </Response>
<?php
        break;
    // Case 3 is for Michael Peterson
    case 3:
?>
        <Response>
          <Dial>+15033839340</Dial>
          <Say>The call failed or the remote party hung up. Goodbye.</Say>
        </Response>
<?php
        break;
    // Case 4 is for our events
    case 4:
?>
        <Response>
          <Say>We don't currently have any events scheduled. Please check back again soon.</Say>
        </Response>
<?php
        break;
?>
<?php
}
?>
