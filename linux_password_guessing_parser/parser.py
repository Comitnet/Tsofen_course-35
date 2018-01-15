from event_line import event_line
import re
from datetime import datetime



'''
TODO:
1) directory mngmt
2) event types (ftp ssh telnet x username valid/invalid x successful x single ip)
3) database
'''

#log_file_name   = "auth.log"
log_file_name   = "auth.log"
#filter_string   = "Failed password"
filter_strings = ["Failed password", "Accepted password"]
timestamp_regex = "^[a-zA-Z]+\s+\d+\s+[\d\:]+"
ip_addr_regex   = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
timestamp_re = re.compile(timestamp_regex)
ipaddress_re = re.compile(ip_addr_regex)

#trigger if 10 events in 30 seconds
event_window_secs   = 5
event_trigger_count = 5

def lineToEventLine(line, attempt_type):
  m  = timestamp_re.search(line)
  dt =  datetime.strptime(m.group(0),'%b  %d %H:%M:%S')\
        .replace(year=datetime.now().year)
  m  = ipaddress_re.search(line)
  el = event_line(dt, m.group(0), attempt_type)
  event_lines.append(el)

count = 0
event_lines = []
with open(log_file_name) as infile:
    for line in infile:
      for f_string in filter_strings:
        if f_string in line:
          print 'found '+f_string+' in line.'
          count += 1
          lineToEventLine(line, f_string)
      '''
        if filter_string in line:
          count += 1
          lineToEventLine(line, Event_Type.FAILED_PASSWORD)
          print line
        elif :
          #re.search("", line).start()
      '''
print "Total failed passwords: "+str(count)
print "=====\n"






upper_pointer = 0
lower_pointer = 0
event_report  = None
events_array  = []
deltas_array  = []
while lower_pointer < len(event_lines) -1:
  lower_pointer += 1
  delta = (event_lines[lower_pointer].event_time - event_lines[upper_pointer].event_time).total_seconds()
  print "("+str(upper_pointer)+","+str(lower_pointer)+") TYPE: "+str(event_lines[lower_pointer].attempt_type)+" In event: "+str(event_report is not None)
  #print "delta: "+str(delta)+"<="+str(event_window_secs)+" counter: "+str(lower_pointer - upper_pointer)+">="+str(event_trigger_count)
  



  if (delta <= event_window_secs) and (lower_pointer - upper_pointer + 1 >= event_trigger_count) and event_report is None:
    event_report = event_lines[upper_pointer]
    events_array.append(event_report)
    print "("+str(upper_pointer)+","+str(lower_pointer)+")"
    #print "EEEEEEEE!!!!!!!!!!!!!!EEEEEEEEEEEE"
  elif delta > event_window_secs and event_report is None:
    upper_pointer += 1

  elif (event_lines[lower_pointer].event_time - event_lines[lower_pointer-1].event_time).total_seconds() >= event_window_secs and event_report is not None:
    print "Event RESET"
    deltas_array.append((event_lines[lower_pointer-1].event_time - event_lines[upper_pointer].event_time).total_seconds())
    event_report = None
    upper_pointer = lower_pointer

  #elif event_report is not None and (event_lines[lower_pointer].event_time - event_lines[lower_pointer-1].event_time).total_seconds() <= event_window_secs:

    #print "upper_pointer += 1"
  

  #print str(delta)+" seconds - ipaddr: "+el.machine_ip_address
  #lower_pointer += 1

for event in events_array:
  print "###start: "+str(event.event_time)
"""   
if event_report is not None:
  print "Event triggered! "+\
        str(lower_pointer - upper_pointer)+\
        " attempts in "+\
        str((event_lines[lower_pointer].event_time - event_lines[upper_pointer].event_time).total_seconds())+\
        " seconds"+\
        " from IP addr: "+str(event_lines[upper_pointer].machine_ip_address)+\
        " at time "+str(event_lines[upper_pointer].event_time)
else:
  print "No events detected"
"""

