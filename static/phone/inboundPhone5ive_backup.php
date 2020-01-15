<?php
    header("content-type: text/xml");
    echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n";
?>
<Response>
    <Gather numDigits="1" action="callerList5ive.php" method="POST">
        <Play loop="1">http://5ivemarketing.com/phone/audio/Memo.mp3</Play>
    </Gather>
</Response>