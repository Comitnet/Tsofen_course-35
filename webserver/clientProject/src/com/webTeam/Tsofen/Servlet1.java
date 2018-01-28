package com.webTeam.Tsofen;

import java.io.*;
import java.util.*;
import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class Serverlet1
 */
@WebServlet("/Servlet1")
public class Servlet1 extends HttpServlet {
	private static final long serialVersionUID = 1L;
	List<Event> myList;
	DataBase data;
	private String host, port, userName, pass, databaseName;

	/**
	 * @see HttpServlet#HttpServlet()
	 */
	public Servlet1() {
		super();

	}

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse
	 *      response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

	}

	// <--!<meta http-equiv="refresh"
	// content="5"url=http://localhost:8080/clientProject/MainPage "/>-->
	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse
	 *      response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		CountObject obj = data.getCountersOfEvents();
		// TODO Auto-generated method stub
		host = request.getParameter("host");
		port = request.getParameter("port");
		userName = request.getParameter("userNmae");
		pass = request.getParameter("pass");
		databaseName = request.getParameter("databaseName");
		data = new DataBase(host, port, userName, pass, databaseName);
		myList = data.getAllEvents();
		request.setAttribute("x", "h");
		request.setAttribute("posts", myList);
		CountObject obj2 = new CountObject(5, 5, 5);
		// request.setAttribute("count", obj2);

		RequestDispatcher dispatcher = getServletContext().getRequestDispatcher("/MainPage.jsp");

		dispatcher.forward(request, response);

	}

}
