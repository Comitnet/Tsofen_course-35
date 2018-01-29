<?xml version="1.0" encoding="UTF-8" ?>
<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<!DOCTYPE html">
<%
	if (session.getAttribute("user") == null)
		response.sendRedirect("login.html");
%>
<%@ page import="java.io.*,java.util.*, java.lang.String"%>
<%@ page import="javax.servlet.*,java.text.*"%>
<html lang="en">
<meta http-equiv="refresh" content="180"url=http://localhost:8080/servlets/ServletEvent.java "/>
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">

<meta name="viewport"
	content="width=device-width, initial-scale=1, shrink-to-fit=no">
<meta name="description" content="">
<meta name="author" content="">
<title>Cyber Project</title>
<link href="css2.css" rel="stylesheet">
	<!-- Bootstrap core CSS-->
<link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
	<!-- Custom fonts for this template-->
<link href="vendor/font-awesome/css/font-awesome.min.css"
	rel="stylesheet" type="text/css">
	<!-- Page level plugin CSS-->
<link href="vendor/datatables/dataTables.bootstrap4.css"
	rel="stylesheet">
<link href="css/sb-admin.css" rel="stylesheet">
 <script>
            $(document).ready(function() {
                var reloadData = 0; // store timer

                // load data on page load, which sets timeout to reload again
                loadData();
            });

            function loadData() {
                $('#load_me').load('events.jsp', function() {
                    if (reloadData != 0)
                        window.clearTimeout(reloadData);
                    reloadData = window.setTimeout(loadData, 10000)
                }).fadeIn("slow"); 
            }
        </script>
</head>

<body>
	<div id=myDiv>
		<h1>Cyber Project</h1>
		<div>
			<div class="container-fluid">
				<!-- Icon Cards-->
				<div class="row">
					<div class="col-xl-3 col-sm-6 mb-3">
						<div class="card text-white bg-primary o-hidden ">
							<div class="card-body">
							
								<div class="mr-5">
									<span id="counter0"></span> Events
								</div>
							</div>

						</div>
					</div>
					<div class="col-xl-3 col-sm-6 mb-3">
						<div class="card text-white bg-success o-hidden ">
							<div class="card-body">
								<div class="mr-5">
									<span id="counter1"></span> Low priority
								</div>
							</div>

						</div>
					</div>
					<div class="col-xl-3 col-sm-6 mb-3">
						<div class="card text-white bg-warning o-hidden ">
							<div class="card-body">
								<div class="mr-5">
									<span id="counter2"></span> Meduim priority
								</div>
							</div>

						</div>
					</div>
					<div class="col-xl-3 col-sm-6 mb-3">
						<div class="card text-white bg-danger o-hidden ">
							<div class="card-body">
								
								<div class="mr-5">
									<span id="counter3"></span> High priority
								</div>
							</div>

						</div>
					</div>
				</div>
				<%
					Date dNow = new Date();
					SimpleDateFormat ft = new SimpleDateFormat("'last update in' dd.MM.yyyy 'at' hh:mm:ss ");
					out.print("<h2 align=\"center\">" + ft.format(dNow) + "</h2>");
				%>
				<!-- Example DataTables Card-->
				<div class="card mb-3">
					<div class="card-header">
						<i class="fa fa-table"></i> show events
					</div>
					<div class="card-body">
						<div class="table-responsive">
							<table class="table table-bordered" id="dataTable" width="100%"
								cellspacing="0">
								<thead>
									<tr>
										<th>ID</th>
										<th>Event name</th>
										<th>Time Date</th>
										<th>Host Details</th>
										<th>security Level</th>
										<th>summary</th>
										<th>FileName</th>
										<th>advanceDetails</th>
									</tr>
								</thead>

								<tbody id="events">

								</tbody>
							</table>
						</div>
					</div>
				</div>
			</div>
			<!-- /.container-fluid-->
			<!-- /.content-wrapper-->
			<!-- Bootstrap core JavaScript-->
			<script src="vendor/jquery/jquery.min.js"></script>
			<script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
			<!-- Core plugin JavaScript-->
			<script src="vendor/jquery-easing/jquery.easing.min.js"></script>
			<!-- Page level plugin JavaScript-->
			<script src="vendor/datatables/jquery.dataTables.js"></script>
			<script src="vendor/datatables/dataTables.bootstrap4.js"></script>
			<!-- Custom scripts for all pages-->
			<script src="js/sb-admin.min.js"></script>
			<!-- Custom scripts for this page-->

			<script src="js/event.js"></script>

		</div>
	</div>
</body>

</html>