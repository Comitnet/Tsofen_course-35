<%@ page language="java" contentType="text/html; charset=windows-1255"
	pageEncoding="windows-1255"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<link rel="stylesheet" type="text/css" href="css2.css">
<meta http-equiv="Content-Type"
	content="text/html; charset=windows-1255">
<title>Insert title here</title>
</head>
<body>
	<h1>Cyber Project</h1>

		<form action="Servlet1" method="post" >
			Host:<br> <input type="text" name="host" value="localhost"><br>
			Port: <br>
			<input type="text" name="port" value="3306"><br> User
			name: <br>
			<input type="text" name="userNmae" value="root"><br>
			password:<br> <input type="text" name="pass" value="admin"><br>
			Database name:<br> <input type="text" name="databaseName"
				value="sys"><br>
			<br> <input type="submit" value="Run">
		</form>
	
</body>
</html>


