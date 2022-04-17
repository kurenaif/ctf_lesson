<?php
function base64_urlsafe_encode($val) {
	$val = base64_encode($val);
	return str_replace(array('+', '/'), array('_', '-'), $val);
}

function base64_urlsafe_decode($val) {
	$val = str_replace(array('_','-'), array('+', '/'), $val);
	return base64_decode($val);
}


$plaintext = "message to be encrypted";
$cipher = "aes-128-gcm";
$key = "0000000000000000";
$ciphertext = base64_urlsafe_decode($_GET['ciphertext']);
$tag = base64_urlsafe_decode($_GET['tag']);
$iv = base64_urlsafe_decode($_GET['iv']);

$original_plaintext = openssl_decrypt($ciphertext, $cipher, $key, $options=0, $iv, $tag);
echo $original_plaintext."\n";
?>

