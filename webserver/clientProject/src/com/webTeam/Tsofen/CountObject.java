package com.webTeam.Tsofen;

public class CountObject {
	private int allEvent=0;
	public int getAllEvent() {
		return allEvent;
	}
	public void setAllEvent(int m,int l, int h) {
		this.allEvent = m+l+h;
	}
	public int getLow() {
		return low;
	}
	public void setLow(int low) {
		this.low = low;
	}
	public CountObject(int low, int hight, int medium) {
		super();
		this.low = low;
		this.hight = hight;
		this.medium = medium;
	}
	public int getHight() {
		return hight;
	}
	public void setHight(int hight) {
		this.hight = hight;
	}
	public int getMedium() {
		return medium;
	}
	public void setMedium(int medium) {
		this.medium = medium;
	}
	private int low=0;
	private int hight=0;
	private int medium=0;

}
