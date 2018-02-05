
 var c1=0;
 var c2=0;
 var c3=0;
$(document).ready(function() {
    $.get("Events?func=getEvents", function(eventsdata) {
        $('#events').html("");
       
        for (var i = 0; i < eventsdata.length; i++) {
           
            $('#events').append( "<tr id=tr"+i+">").css('font','bold 15px arial, sans-serif');
            $('#events').append("<td id=td" + i +'0'   +">" + eventsdata[i].id + "</td>");
            $('#events').append("<td id=td" + i + '1' + ">" + eventsdata[i].eventname + "</td>");
            $('#events').append("<td id=td" + i + '2' + ">" + eventsdata[i].TimeDate + "</td>");
            $('#events').append("<td id=td" + i + '3' + ">" + eventsdata[i].HostDetails + "</td>");
            $('#events').append("<td id=td" + i + '4' + ">" + eventsdata[i].securityLevel + "</td>");
            $('#events').append("<td id=td" + i + '5' + ">" + String(eventsdata[i].summary) + "</td>");
            $('#events').append("<td id=td" + i + '6' + ">" + eventsdata[i].FileName + "</td>");
            $('#events').append("<td id=td" + i + '7' + ">" + String(eventsdata[i].advanceDetails) + "</td>");
            $('#events').append("</tr>");
           
                			switch(eventsdata[i].securityLevel) {
                            case "Low":
                            	$('#td' + i +'0').css('color', '#009900');
                            	$('#td' + i +'1').css('color', '#009900');
                            	$('#td' + i +'2').css('color', '#009900');
                            	$('#td' + i +'3').css('color', '#009900');
                            	$('#td' + i +'4').css('color', '#009900');
                            	$('#td' + i +'5').css('color', '#009900');
                            	$('#td' + i +'6').css('color', '#009900');
                            	$('#td' + i +'7').css('color', '#009900');
                            	c1=c1+1;
                                break;
                            case "Medium":
                            	$('#td' + i +'0').css('color', '#ff9900');
                            	$('#td' + i +'1').css('color', '#ff9900');
                            	$('#td' + i +'2').css('color', '#ff9900');
                            	$('#td' + i +'3').css('color', '#ff9900');
                            	$('#td' + i +'4').css('color', '#ff9900');
                            	$('#td' + i +'5').css('color', '#ff9900');
                            	$('#td' + i +'6').css('color', '#ff9900');
                            	$('#td' + i +'7').css('color', '#ff9900');
                            	c2=c2+1;
                                break;
                            case "High":
                            	$('#td' + i +'0').css('color', '#ff0000');
                            	$('#td' + i +'1').css('color', '#ff0000');
                            	$('#td' + i +'2').css('color', '#ff0000');
                            	$('#td' + i +'3').css('color', '#ff0000');
                            	$('#td' + i +'4').css('color', '#ff0000');
                            	$('#td' + i +'5').css('color', '#ff0000');
                            	$('#td' + i +'6').css('color', '#ff0000');
                            	$('#td' + i +'7').css('color', '#ff0000');
                            	c3=c3+1;
                            	break;
                        }
                
        }
    }).done(function() {
        
            $('#counter0').html(c1+c2+c3);
            $('#counter1').html(c1);
            $('#counter2').html(c2);
            $('#counter3').html(c3);


     
    });
});