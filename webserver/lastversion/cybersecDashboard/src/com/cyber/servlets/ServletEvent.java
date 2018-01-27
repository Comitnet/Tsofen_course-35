package com.cyber.servlets;

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.SQLException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import com.cyber.db.EventQuery;
import com.cyber.db.MyConnection;


/**
 * Servlet implementation class GetKpiData
 */
@WebServlet("/Events")
public class ServletEvent extends HttpServlet {
	
	private static final long serialVersionUID = 1L;
	
    /**
     * @see HttpServlet#HttpServlet()
     */
    public ServletEvent() { super(); }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException{
		
		MyConnection con = null;
		PrintWriter out = response.getWriter();
		String func = request.getParameter("func");
		HttpSession session = request.getSession();
		con = (MyConnection)session.getAttribute("connection");
		response.setContentType("application/json");
		response.setCharacterEncoding("utf-8");
		
		if (con == null) {
    		
    		try { con = new MyConnection(); }
    		catch (ClassNotFoundException e) { e.printStackTrace();} 
    		catch (SQLException e) { e.printStackTrace(); }
    		
    		session.setAttribute("connection",con);
    	}	
	   
		
		try {
			if(func.equals("getnumEvents")){
				out.print(EventQuery.getnumberEvents(con.getCon()));
			}
			else if(func.equals("getEvents")){
				///// override 
				out.print(EventQuery.getEvents(con.getCon()));
			}
		}catch(SQLException e){ e.printStackTrace(); }
		
		out.close();
	}
}
