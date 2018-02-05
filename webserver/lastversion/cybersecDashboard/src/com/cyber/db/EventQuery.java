package com.cyber.db;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import com.google.gson.JsonArray;
import com.google.gson.JsonObject;

public class EventQuery {
	
	private static Statement st;
	private static ResultSet rs;
	private static String query;
	private static JsonArray jArr;
	private static JsonObject jObj;
	
	
	private EventQuery(){ super(); }

	
	private static void runQuery(Connection con) throws SQLException{
		st = con.createStatement();
		rs = st.executeQuery(query);
	}
	
	
	private static String prepareJsonArray() throws SQLException{
		
		jArr = new JsonArray();
		while(rs.next()){
			jObj = new JsonObject();
			jObj.addProperty("id", rs.getString(1));
			jObj.addProperty("eventname", rs.getString(2));
			jObj.addProperty("TimeDate", rs.getString(3));
			jObj.addProperty("HostDetails", rs.getString(4));
			jObj.addProperty("securityLevel", rs.getString(5));
			jObj.addProperty("summary", rs.getString(6));
			jObj.addProperty("FileName", rs.getString(7));
			jObj.addProperty("advanceDetails", rs.getString(8));
			jArr.add(jObj);
		}
		
        return jArr.toString();
	}
	
	
	public static String getDates(Connection con) throws SQLException{
		
		jArr = new JsonArray();
		st = con.createStatement();
		st.execute("USE KPI;");
		query = "SELECT * FROM Dates;";
		runQuery(con);
		
		while(rs.next()){
			jObj = new JsonObject();
			jObj.addProperty("date", rs.getDate(1).toString());
			jArr.add(jObj);
		}
	
        return jArr.toString();
	}
	
	
	public static String getExchanges(Connection con) throws SQLException{
		
		query = "SELECT * FROM Exchanges;";
		runQuery(con);
		return prepareJsonArray();
	}	
	
	
	public static String getEvents(Connection con) throws SQLException{
	
		query = "SELECT events.id, typeevents.Name as eventname,events.TimeStamp as TimeDate," + 
				"concat( host.HostName,' ',host.mac) as HostDetails, TypeEvents.Severity as SecurityLevel,events.summary ,events.FileName,events.advancedDetails " + 
				"FROM EVENTS   inner JOIN host on events.HostID = host.id  " + 
				"inner JOIN typeevents on typeevents.ID = events.EventId";
		runQuery(con);
		return prepareJsonArray();
	}

	
	public static String getnumberEvents(Connection con) throws SQLException{
		
		query = "select typeevents.Severity,count(*)" + 
				"from events" + 
				"inner join typeevents on events.EventId=typeevents.ID" + 
				"group by typeevents.Severity " + 
				"union all" + 
				"select  distinct typeevents.Severity,0" + 
				"from typeevents" + 
				"where typeevents.Severity not in (select typeevents.Severity" + 
				"from events" + 
				"inner join typeevents on events.EventId=typeevents.ID" + 
				"group by typeevents.Severity )";

		runQuery(con);
		/*\
		 * low
		 * meduim
		 * hight
		 */
		jObj = new JsonObject();
		while(rs.next()){
			switch(rs.getString(1)) {
			case "Low":	jObj.addProperty("L", rs.getString(2).trim());	break;
			case "Medium":jObj.addProperty("M", rs.getString(2).trim());break;
			case "High":jObj.addProperty("H", rs.getString(2).trim());break;
			}
			jArr.add(jObj);
		}
		return jObj.toString();
	}
	
	
	public static String getGroups(Connection con, String exchId, String advId, String campId, String fromDate, String toDate) throws SQLException{
		
		query = "SELECT DISTINCT Groups.groupID, Groups.groupName"
			  + " FROM Groups INNER JOIN Exch_Group"
			  + " WHERE Groups.groupID=Exch_Group.groupID" 
			  +	" AND Exch_Group.exchangeID=" + exchId
			  +	" AND Groups.advertiserID=" + advId
			  +	" AND Groups.campaignID=" + campId
			  +	" AND Exch_Group.eventDate BETWEEN '" + fromDate + "' AND '"+ toDate +"';";

		runQuery(con);
		return prepareJsonArray();
	}
	
	
	public static String getCreatives(Connection con,String exchId, String advId, String campId, String groupId,String fromDate,String toDate) throws SQLException{
		
		query = "SELECT DISTINCT Creatives.creativeID, Creatives.creativeName"
			  + " FROM Creatives,Exch_Creative,Camp_Creative,Group_Creative"
			  + " WHERE Creatives.creativeID=Exch_Creative.creativeID"
			  + " AND Creatives.creativeID=Camp_Creative.creativeID"
			  + " AND Exch_Creative.exchangeID="+exchId
			  + " AND Creatives.advertiserId="+advId
			  + " AND Camp_Creative.campaignID="+campId
			  + " AND Group_Creative.groupID="+groupId
			  + " AND Exch_Creative.eventDate BETWEEN '"+ fromDate +"' AND '"+ toDate +"'";

		runQuery(con);
		return prepareJsonArray();
	}


	public static String getGraphJson(Connection con,String exchId, String advId, String campId, String groupId, String creativeId, String fromDate,String toDate) throws SQLException{
		
		jArr = new JsonArray();
	
		query = "SELECT eventDate,SUM(impressions) AS impressions,SUM(clicks) AS clicks"
			  + " FROM MAINTABLE"
			  + " WHERE exchangeID="+exchId
			  + " AND advertiserID="+advId
			  + " AND campaignID="+campId
			  + " AND groupID="+groupId
			  + " AND creativeID="+creativeId
			  + " AND eventDate BETWEEN '"+ fromDate +"' AND '"+ toDate +"'"
			  + " GROUP BY eventDate;";

		runQuery(con);
		
		while(rs.next()){
			jObj = new JsonObject();
			jObj.addProperty("date", rs.getDate(1).toString());
			jObj.addProperty("impressions", rs.getInt(2));
			jObj.addProperty("clicks", rs.getInt(3));
			jArr.add(jObj);
		}
		
	    return jArr.toString();
	}

	
	public static void close_RS_ST() throws SQLException{
		st.close();
		rs.close();
	}
}
