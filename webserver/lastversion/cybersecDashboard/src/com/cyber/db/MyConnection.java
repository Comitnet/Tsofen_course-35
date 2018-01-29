package com.cyber.db;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;


public class MyConnection {
	
	private Connection con;
	private final String url = "jdbc:mysql://localhost:3306/version2";
	private final String username = "root";
	private final String pass = "admin";
	
	public MyConnection() throws ClassNotFoundException, SQLException{
		
		Class.forName("com.mysql.jdbc.Driver");
		con = DriverManager.getConnection(url ,username ,pass);
	}
	
	public Connection getCon(){ return con; }
	
	public void closeCon() throws SQLException { con.close(); }

}
