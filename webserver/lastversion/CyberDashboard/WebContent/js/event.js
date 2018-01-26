
$(document).ready(function() {
	$.get("Events?func=getEvents", function(eventsdata){
        $('#events').html( ""); 
        for(var i = 0; i < eventsdata.length; i++){
            $('#events').append( "<tr>"); 
            $('#events').append( "<td>"+eventsdata[i].id+"</td>"); 
            $('#events').append( "<td>"+eventsdata[i].eventname+"</td>"); 
        	$('#events').append( "<td>"+eventsdata[i].TimeDate+"</td>"); 
        	$('#events').append( "<td>"+eventsdata[i].HostDetails+"</td>"); 
        	$('#events').append( "<td>"+eventsdata[i].securityLevel+"</td>"); 
            $('#events').append( "<td>"+String(eventsdata[i].summary).substr(0,15)+"</td>"); 
            $('#events').append( "<td>"+eventsdata[i].FileName+"</td>"); 
        	$('#events').append( "<td>"+String(eventsdata[i].advanceDetails).substr(0,15)+"</td>"); 
            $('#events').append( "</tr>"); 
/*
			jObj.addProperty("id", rs.getString(1));
			jObj.addProperty("eventname", rs.getString(2));
			jObj.addProperty("TimeDate", rs.getString(3));
			jObj.addProperty("HostDetails", rs.getString(4));
			jObj.addProperty("securityLevel", rs.getString(5));
			jObj.addProperty("summary", rs.getString(6));
			jObj.addProperty("FileName", rs.getString(7));
			jObj.addProperty("advanceDetails", rs.getString(8));
*/
        }
    }).done(function(){
    	$.get("Events?func=getnumEvents", function(data){
                $('#counter0').html(parseInt(data.L)+parseInt(data.M)+parseInt(data.H)); 
                $('#counter1').html(data.L); 
                $('#counter2').html(data.M); 
                $('#counter3').html(data.H); 


        });
    });
});



