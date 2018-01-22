package com.webTeam.Tsofen;
/*
<td>${post.id}</td>
<td>${post.hostID}</td>
<td>${post.location}</td>
<td>${post.status}</td>
<td>${post.name}</td>
<td>${post.client}</td>*/
public class Event {//id //eventName TimeDate HostDetails SecurityLevel summary
	private String id;
	private String timeDate;
	private String hostDetails;
	private String securityLevel;
	private String eventName;
	private String summary;
	public String getId() {
		return id;
	}
	public void setId(String id) {
		this.id = id;
	}
	public String getTimeDate() {
		return timeDate;
	}
	public void setTimeDate(String timeDate) {
		this.timeDate = timeDate;
	}
	public String getHostDetails() {
		return hostDetails;
	}
	public void setHostDetails(String hostDetails) {
		this.hostDetails = hostDetails;
	}
	public String getSecurityLevel() {
		return securityLevel;
	}
	public void setSecurityLevel(String securityLevel) {
		this.securityLevel = securityLevel;
	}
	public String getEventName() {
		return eventName;
	}
	public void setEventName(String eventName) {
		this.eventName = eventName;
	}
	public String getSummary() {
		return summary;
	}
	public void setSummary(String summary) {
		this.summary = summary;
	}
	public Event() {
		super();
		// TODO Auto-generated constructor stub
	}
	


	


}
