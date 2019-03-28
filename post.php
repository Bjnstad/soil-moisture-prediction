<?php
error_reporting(E_ALL); ini_set('display_errors', '1');

$servername = "localhost";
$username = "api";
$password = "Panda123";
$dbname = "soilsense";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 


$data = json_decode(file_get_contents('php://input')) ;
 
$id = $data[0];
$sql = "";
foreach ( $data[1] as $v ) {

	$sql .= "INSERT INTO weather_values (date, value, station_sym)
	VALUES ('". $v[0]  ."', '". $v[1]  ."', '". $id ."');";
}

$conn->multi_query($sql);
$conn->close();
?>

