import os
import mysql.connector
import datetime
import sys
sys.path.append("..")



#  update last sync date
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


# list of keywords to help trace a ports scan
PS_keyWordList = ["Consecutive TCP small segments exceeding threshold","TCP session without 3-way handshake"]


HostID = 'fe80a186338986ee61fd'
datesList = []
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
    elif (int(h) == 12):
        h = int(h) 
        convertedFileName = yyyy +'-'+ mm +'-' +dd + ' ' + str(h) +':' + mi +':' +se
    else:
        h = int(h) + 12
        convertedFileName = yyyy +'-'+ mm +'-' +dd + ' ' + str(h) +':' + mi +':' +se
    return convertedFileName


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




# class that contains all the information of the portscan attack
class PortScan(object):

    
    def __init__(self,sourceIP = None,destinatioIP = None,sourcePort = None,destinationPort = None,portCounter = None,line = None, severity = None, smmary = None):

        '''
        sourceIP is reffered to tha attacker ip
        destinationIP is reffered to the attacked IP
        '''
        
        self.sourceIP = sourceIP
        self.destinatioIP = destinatioIP
        self.sourcePort = sourcePort
        self.destinationPort = destinationPort
        self.portCounter = portCounter
        self.line = line
        self.severity = severity
        self.summary = summary

# getting the path of the current dir
cur_dir=os.path.dirname(os.path.realpath(__file__))

# getting the path of the main dir
LogPath = os.path.join(cur_dir, "C:\FTPServer\a")

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
                print "1"
                datesList.append(filedate)
                print datesList
##                if os.stat(filename).st_size == 0:
##                    continue
                with open(os.path.join(subject_path, filename)) as f:
                    lines = f.readlines()
                    
                # a list which includes all the events
                    PS_EventList = []
                # dictionary which contains source ips and their indexes
                    ipList = {}
                    ipIndex = 0
                # num reffers to line number
                    for num, line in enumerate(lines,1):
                        if any(s in line for s in PS_keyWordList):
                            summary = lines[num-1] +lines[num]+ lines[num+1]+lines[num+2]+ lines[num+3]
                            #summary = line
                            lineNumber = num
                            lineSummary = lines[num+1].split(' ')
                            sIP = (lineSummary[1]).split(":")[0]
                            sPort = (lineSummary[1]).split(":")[1]
                            destIP = (lineSummary[3]).split(":")[0]
                            destPort = (lineSummary[3]).split(":")[1]
                            lastDate = convertDnT(lineSummary[0]) 
    #checking out if the source ip exesting and initializing the class for every new ip
                            
                            if not (str(sIP) in ipList):
                                ipList[sIP] = ipIndex
                                ipIndex +=1
                                PS_EventList.append(PortScan(sIP,destIP,sPort,destPort,1,lineNumber,'Low', summary))

    # updatimg 
                            if sIP in ipList:
                                i = ipList[sIP]
                                if destPort not in (PS_EventList[i].destinationPort.split(' ')):
                                    PS_EventList[i].destinationPort = PS_EventList[i].destinationPort+ ' ' + destPort
                                    PS_EventList[i].portCounter += 1
                                    PS_EventList[i].line = str(PS_EventList[i].line) +' '+ str(lineNumber)
                                    PS_EventList[i].summary = PS_EventList[i].summary 
                                    if len(PS_EventList[i].destinationPort.split(' ')) < 3:
                                        PS_EventList[i].severity = 'Low'
                                    elif len(PS_EventList[i].destinationPort.split(' ')) < 6:
                                        PS_EventList[i].severity = 'Medium'
                                    elif len(PS_EventList[i].destinationPort.split(' ')) > 6:
                                        PS_EventList[i].severity = 'High'
                                        
                for j in range(len(ipList)):
                           
                    if PS_EventList[j].severity == 'Low':
                        eventID = 2
                    elif PS_EventList[j].severity == 'Medium':
                        eventID = 3
                    elif PS_EventList[j].severity == 'High':
                        eventID = 4
                            
                    write_to_DB(filedate,eventID,ID,PS_EventList[j].summary,PS_EventList[j].sourceIP,str(PS_EventList[j].line),filename)                            

LastSync = max(datesList)
update_lastSync(max(datesList))
                
