<?php 
  $secret = "12345678";
  assert(strlen($secret) == 8);
  $yourquery = $_SERVER['QUERY_STRING'];
  print_r("<p>".urldecode($yourquery)."</p>");
  
  $MAC = hash("sha256",$secret.urldecode($yourquery));
  
  if (isset($_GET["username"])){
    if ($_GET["username"] === "admin"){
      if ($_COOKIE["signature"] === $MAC){
         print_r($flag);
      } else {
         print_r("BAD SIGNATURE!");
      }
    } else if ($_GET["username"] === "guest"){
      print_r("Welcome Guest.  Here is a signature: ");
      print_r(hash("sha256",$secret."username=guest")); 
    }
  } else {
    print_r("USAGE: ?username={guest,admin}");
  }
  print_r("<hr>"); 
  highlight_file(__FILE__);
?>