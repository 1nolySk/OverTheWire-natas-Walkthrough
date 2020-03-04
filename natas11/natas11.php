<?php


	function xor_encrypt($in) {
	    $key = base64_decode("ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw=");
	    $text = $in;
	    $outText = '';

	    // Iterate through each character
	    for($i=0;$i<strlen($text);$i++) {
	    	$outText .= $text[$i] ^ $key[$i % strlen($key)];
	    }

	    return $outText;
	}

	$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");

	$res = xor_encrypt(json_encode($defaultdata));

	print("Key Pattern : ".$res);

	
	//Generate new cookie

	$key = 'qw8J';

	$data = json_encode(array( "showpassword"=>"yes", "bgcolor"=>"#ffffff"));

	$outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($data);$i++) {
    	$outText .= $data[$i] ^ $key[$i % strlen($key)];
    }

    $output = base64_encode($outText);

    print("\tNew cookie : ". $output);
?>