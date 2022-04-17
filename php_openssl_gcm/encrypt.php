<?php
function base64_urlsafe_encode($val) {
	$val = base64_encode($val);
	return str_replace(array('+', '/', '='), array('_', '-', ''), $val);
}

function base64_urlsafe_decode($val) {
	$val = str_replace(array('_','-'), array('+', '/'), $val);
	return base64_decode($val);
}

$plaintext = "message to be encrypted";
$cipher = "aes-128-gcm";
$key = "0000000000000000";
if (in_array($cipher, openssl_get_cipher_methods()))
{
    $ivlen = openssl_cipher_iv_length($cipher);
    $iv = openssl_random_pseudo_bytes($ivlen);
    $ciphertext = openssl_encrypt($plaintext, $cipher, $key, $options=0, $iv, $tag);
	
	$ciphertext = base64_urlsafe_encode($ciphertext);
	$tag = base64_urlsafe_encode($tag);
	$iv =base64_urlsafe_encode($iv);

	echo "http://localhost:8000/decrypt.php?";
	echo "ciphertext=".$ciphertext."&";
	echo "tag=".$tag."&";
	echo "iv=".$iv."";

	$ciphertext = base64_urlsafe_decode($ciphertext);
	$tag = base64_urlsafe_decode($tag);
	$iv = base64_urlsafe_decode($iv);

	$original_plaintext = openssl_decrypt($ciphertext, $cipher, $key, $options=0, $iv, $tag);
	// echo $original_plaintext."\n";
}
?>
