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

    public function __destruct()
    {
        $this->call();
    }
}

$obj = unserialize(base64_urlsafe_decode($_GET["obj"]));