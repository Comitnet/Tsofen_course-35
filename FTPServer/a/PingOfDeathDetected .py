import os
import mysql.connector
import datetime
import sys
sys.path.append("..")
now = datetime.datetime.now()
datesList = []

HostID = 'fe80a186338986ee61fd'

def update_lastSync(lastSync):
    cnx = mysql.connector.connect(user='root', password='admin',host='localhost',database='version2')
    cursor = cnx.cursor()
    
    add_event = ("update `version2`.`host` set `lastSync`='"+lastSync +"' where ID like '1'")            
    # Add Event 
    cursor.execute(add_event)
    
    # Make sure data is committed to the database
    cnx.commit()

    cursor.close()
    cnx.close()


# function that compares the name of the file with the last synchronized date
def analysedFile(date,lastSync):
    yyyy = date[0] +date[1] +date[2]+date[3]
    mm = date[4] +date[5]
    dd = date[6] +date[7]
    hh = date[8] +date[9]
    mm = date[10] +date[11]
    ss = date[12] +date[13]
    filedate 
    return str(fileDate)>lastSync

# function that converts date and time to the same format of the db
def convertDnT(date):
    now = datetime.datetime.now()
    timeSplit = date.split('-')#01/27-18:43:07.321251
    m = (timeSplit[0]).split('/')[0] # 01/27
    d = (timeSplit[0]).split('/')[1]
    h = (timeSplit[1]).split(':')[0] #18:43:07.321251
    mi = (timeSplit[1]).split(':')[1]
    se = ((timeSplit[1]).split(':')[2]).split('.')[0]
    time=str(now.year) +"-"+m+"-"+d+" "+h+":"+mi+":"+se
    return time

# function that cuts the date and time of the filename

def convertFileName(fname):
    '''
    spliting file name and converting it to date and time
    '''
    fnsplit = fname.split('_Snort_')
    fnsplit1 = fnsplit[1].split(' ')
    dd = fnsplit1[0].split('-')[1]
    mm = fnsplit1[0].split('-')[0]
    yyyy = fnsplit1[0].split('-')[2]

    h = fnsplit1[1].split('-')[0]
    mi = fnsplit1[1].split('-')[1]
    se = fnsplit1[1].split('-')[2]

    if (fnsplit1[2] == "AM"):
        convertedFileName = yyyy +'-'+ mm +'-' +dd + ' ' + h +':' + mi +':' +se
    else:
        if (int(h) == 12):
            convertedFileName = yyyy +'-'+ mm +'-' +dd + ' ' + str(h) +':' + mi +':' +se
        else:
            h = int(h) + 12
            convertedFileName = yyyy +'-'+ mm +'-' +dd + ' ' + str(h) +':' + mi +':' +se
    return convertedFileName



def update_lastSync(lastSync):
    cnx = mysql.connector.connect(user='root', password='admin',host='localhost',database='version2')
    cursor = cnx.cursor()
    
    add_event = ("update `version2`.`host` set `lastSync`='"+lastSync +"' where ID like '1'")            
    # Add Event 
    cursor.execute(add_event)
    
    # Make sure data is committed to the database
    cnx.commit()

    cursor.close()
    cnx.close()


# function that writes information to the db

def write_to_DB(TimeStamp,eventID,HostID,summary,attacker,advancedDetails,fileName):
    cnx = mysql.connector.connect(user='root', password='admin',host='localhost',database='version2')
    cursor = cnx.cursor()
    
    add_event = ("INSERT INTO `version2`.`events` (`TimeStamp`, `EventId`, `HostID`, `summary`,`attacker`,`advancedDetails`,`FileName`)VALUES ('"+TimeStamp+"','"+str(eventID)+"','"+str(HostID)+"','"+summary+"','"+attacker+"','"+str(advancedDetails)+"','"+fileName+"');")
            
    # Add Event 
    cursor.execute(add_event)
    
    # Make sure data is committed to the database
    cnx.commit()

    cursor.close()
    cnx.close()


class PingAttack(object):
    #__init__() functions as the class constructor
    def __init__(self,keyinMap=None, ipSrc=None,ipDes=None, summry=None, advanced_details=None, time=None, severity_level=None, file_name_index=None):
       self.keyinMap=keyinMap
       self.ipSrc=ipSrc
       self.ipDes=ipDes
       self.summry=summry
       self.advanced_details=advanced_details
       self.time=time
       self.severity_level=severity_level
       self.file_name_index=file_name_index
# save IPSur-IpDes-PacketSize

##personList = []
##personList.append(Person("Payne N. Diaz", "coach", "Without exception, there is no rule!"))



# getting the path of the current dir
cur_dir=os.path.dirname(os.path.realpath(__file__))

# getting the path of the main dir
LogPath = os.path.join(cur_dir, "a")

#reading files from different dirs, (dirname -> dubdirname-> filename
for dirname, dirnames, filenames in os.walk('.'):
    for subdirname in dirnames:
# connecting to db
        cnx = mysql.connector.connect(user='root', password='admin',host='localhost',database='version2')
        cursor = cnx.cursor()
        select_mac_details = ("SELECT ID , LastSync from version2.host where mac like '"+subdirname+"'")
        cursor.execute(select_mac_details)
        
        for (ID,LastSync) in cursor:
            print(ID , LastSync)
            
        cursor.close()
        cnx.close()
        c = 0
        subject_path = os.path.join(dirname, subdirname)
        for filename in os.listdir(subject_path):
            filedate = convertFileName(filename)
            print filedate
            if filedate > str(LastSync):
                datesList.append(filedate)
                with open(os.path.join(subject_path, filename)) as f:
                    #lines = f.readlines()
                    searchstringsAttack = ('PingOfDeathDetected')

                    EventsList=[]
                    sourceMap = {}
                    rows=(f.read()).split('\n')
                    for index,line in enumerate(rows):
                        if searchstringsAttack in line:
                            summry=rows[index]+'\n'+rows[index+1]+'\n'+rows[index+2]+'\n'+rows[index+3]+'\n'+rows[index+4]
                            #----------------------------------------row1 in Attack #  print (rows[index+2])#01/17-19:51:15.352526 172.16.15.55 -> 172.16.15.100 
                            arr1=(rows[index+2]).split(' ')
                            timeSplit=arr1[0].split('-')#01/27-18:43:07.321251
                            m=(timeSplit[0]).split('/')[0] # 01/27
                            d=(timeSplit[0]).split('/')[1]
                            h=(timeSplit[1]).split(':')[0] #18:43:07.321251
                            mi=(timeSplit[1]).split(':')[1]
                            time=str(now.year) +"-"+m+"-"+d+" "+h+":"+mi
                            ips=arr1[1]
                            ipd=arr1[3]
                            #----------------------------------------row2 in Attack
                            size=((((rows[index+3]).split(' '))[5]).split(':'))[1]
                            index +=4
                            s=ips+"->"+ipd+" Size="+size 
                            if s in sourceMap:
                                sourceMap[s] += 1
                            else:             
                                EventsList.append(PingAttack(s,ips,ipd,summry,size,time,"",str(index)))
                                sourceMap[s] = 1
                              

                    i=0;
                    for a in EventsList:
                       if (sourceMap.get(EventsList[i].keyinMap) <4):
                          EventsList[i].severity_level="Low"
                          eventID = 4
                          #Insert To Data Base Event
##                          print( "IP-source: "+EventsList[i].ipSrc)
##                          print( "IP-destination: "+EventsList[i].ipDes)
##                          print( "Date_Time: "+EventsList[i].time)
##                          print( "severity_level: "+EventsList[i].severity_level)
##                          print( "begin in row number: "+EventsList[i].file_name_index)
##                          print( "summry: "+EventsList[i].summry)
##                          print( "============================================================================")
                          write_to_DB(filedate,eventID,ID,EventsList[i].summry,EventsList[i].ipSrc,EventsList[i].file_name_index,filename)
                          
                          
                       elif( sourceMap.get(EventsList[i].keyinMap) <8) :
                          EventsList[i].severity_level="Medium"
                          eventID = 5
                          #Insert To Data Base Event
##                          print( "IP-source: "+EventsList[i].ipSrc)
##                          print( "IP-destination: "+EventsList[i].ipDes)
##                          print( "Date_Time: "+EventsList[i].time)
##                          print( "severity_level: "+EventsList[i].severity_level)
##                          print( "begin in row number: "+EventsList[i].file_name_index)
##                          print( "summry: "+EventsList[i].summry)
##                          print( "============================================================================")
                          write_to_DB(filedate,eventID,ID,EventsList[i].summry,EventsList[i].ipSrc,EventsList[i].file_name_index,filename)
                       else:
                          EventsList[i].severity_level="High"
                          eventID = 6
                          #Insert To Data Base Event
##                          print( "IP-source: "+EventsList[i].ipSrc)
##                          print( "IP-destination: "+EventsList[i].ipDes)
##                          print( "Date_Time: "+EventsList[i].time)
##                          print( "severity_level: "+EventsList[i].severity_level)
##                          print( "begin in row number: "+EventsList[i].file_name_index)
##                          print( "summry: "+EventsList[i].summry)
##                          print( "============================================================================")
                          write_to_DB(filedate,eventID,ID,EventsList[i].summry,EventsList[i].ipSrc,EventsList[i].file_name_index,filename)
                       i+=1
   
##    
##                    for j in range(len(ipList)):
##                           
##                    if PS_EventList[j].severity == 'Low':
##                        eventID = 2
##                    elif PS_EventList[j].severity == 'Medium':
##                        eventID = 3
##                    elif PS_EventList[j].severity == 'High':
##                        eventID = 4
##
##                            #print (filedate,eventID,ID,PS_EventList[j].summary,PS_EventList[j].sourceIP,PS_EventList[j].line,filename)
##                            
##                    #write_to_DB(filedate,eventID,ID,PS_EventList[j].summary,PS_EventList[j].sourceIP,str(PS_EventList[j].line),filename)
##
