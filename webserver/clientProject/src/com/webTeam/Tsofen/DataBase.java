package com.webTeam.Tsofen;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

import javax.sql.rowset.CachedRowSet;

public class DataBase {
	private Connection connDB;
	private String address;
	private String port;
	private String username;
	private String password;
	private String database;

	public DataBase(String address, String port, String username, String password, String database) {
		super();
		this.connDB = null;
		this.database = database;
		this.port = port;
		this.username = username;
		this.password = password;
		this.address = address;
		conn();
	}

	void conn() {
		try {
			Class.forName("com.mysql.jdbc.Driver").newInstance();
			String connString = "jdbc:mysql://" + this.address + ":" + this.port + "/" + this.database;
			Connection conn = DriverManager.getConnection(connString, this.username, this.password);
			this.connDB = conn; 
		} catch (Exception ex) {
			 System.out.println(ex);
		}
	}

	public Connection getConnection() {
		if (this.connDB != null)
			return this.connDB;
		conn();
		return this.connDB;
	}

	public List<Event> getAllEvents() {
		List<Event> events = new ArrayList<Event>();
		try {
			Statement statement = getConnection().createStatement();
			ResultSet resultSet = statement.executeQuery(
					"SELECT events.id,"
			        +"  events.EventName as eventName,"
			        +"events.TimeStamp as TimeDate,"
					+"concat( host.HostName, \"    \", hostmac.ip) as hostDetails,"
			        +" TypeEvents.Severity as SecurityLevel,"
					+"events.summary  FROM "
					+ database.trim()
					+ ".EVENTS"
					+"   inner JOIN hostmac on events.HostID = hostmac.id  "
					+"inner JOIN typeevents on TypeEvents.name = events.EventName "
					+" inner join host on host.id=hostmac.id" 
					+";");
			while (resultSet.next()) {
				Event event = new Event();
				event.setId(resultSet.getString("id"));
				event.setTimeDate(resultSet.getString("TimeDate"));
				event.setEventName(resultSet.getString("eventName"));
				event.setSummary(resultSet.getString("summary"));
				event.setSecurityLevel(resultSet.getString("SecurityLevel"));
				event.setHostDetails(resultSet.getString("hostDetails"));
				events.add(event);
				
			}
			resultSet.close();
			statement.close();
			return events;
		} catch (SQLException e) {
			System.out.println(e.getMessage());
			return null;
		}

	}
	
	
	public CountObject getCountersOfEvents() {
		HashMap<String, Integer> myMap=new HashMap<String,Integer>();
		try {
				Statement statement = getConnection().createStatement();
			ResultSet resultSet = statement.executeQuery(
					"from events\r\n" + 
					"inner join typeevents on events.EventName=typeevents.Name\r\n" + 
					"group by typeevents.Severity \r\n" + 
					"union all\r\n" + 
					"select  distinct typeevents.Severity,0\r\n" + 
					"from typeevents\r\n" + 
					"where typeevents.Severity not in (select typeevents.Severity\r\n" + 
					"from events\r\n" + 
					"inner join typeevents on events.EventName=typeevents.Name\r\n" + 
					"group by typeevents.Severity )");
			while (resultSet.next()) {
				myMap.put(String.valueOf(resultSet.getInt("Severity")), resultSet.getInt("count"));
			}
				CountObject countObject=new CountObject(myMap.get("low"), myMap.get("hight"),myMap.get("medium"));
				countObject.setAllEvent(myMap.get("low"), myMap.get("hight"),myMap.get("medium"));
			resultSet.close();
			statement.close();
			
			return countObject;
		} catch (Exception e) {
			System.out.println(e.getMessage());
			return null;
		}

	}
}
