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
	$user_name = $_GET["user_name"];
	$pass = $_GET["pass"];
	$email = $_GET["email"];
	
		$query = "Select * from user where username ='$user_name' AND password ='$pass'";
		$result = $conn->query($query);
		if ($result->num_rows != 0 )
		{
			echo "User already exist";
		}else 
		{
			$sql = "INSERT INTO `user` (`id`, `username`, `password`, `email`) VALUES (NULL, '$user_name', '$pass', '$email')";
			if($conn->query($sql))
			{
				echo "Sucessful regist";
			}else{
				echo "erro".$conn->error;
			}	
			
		}
	
	$conn->close();
?>