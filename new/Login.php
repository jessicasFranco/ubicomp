<?php
	$servername = "localhost:3306";
	$username = "root";
	$password = "root";
	$dbname = "wearweather";
	//create conncetion
	$conn = new mysqli($servername,$username, $password,$dbname);
	if($conn->connect_error)
	{
		die("Connection failed: ".$conn->connect_error);
		echo("ERRO");
	}
	$user_name = $_GET["username"];
	$password = $_GET["pass"];
	$sql ="SELECT * FROM user where username = '$user_name' and password = '$password'";
	$result = $conn->query($sql);
	if($result->num_rows > 0)
	{
		echo "user exists";
	}else{
		echo "false";
	}
	$conn->close();

?>