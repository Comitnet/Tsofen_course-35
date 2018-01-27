package com.cyber.db;

import java.sql.SQLException;

public class test {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		MyConnection con;
		try {
			con = new MyConnection();
			System.out.println(EventQuery.getEvents(con.getCon()));

		} catch (ClassNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} 



	}

}
