<?php

$key = "3d3d516343746d4d6d6c315669563362";

$res = base64_decode(strrev(hex2bin($key)));

print($res);

// run using terminal on linux : php natas8.php

?>