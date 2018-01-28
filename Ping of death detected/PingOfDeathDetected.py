import datetime
now = datetime.datetime.now()
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
EventsList=[]
sourceMap = {}# save IPSur-IpDes-PacketSize
'''
personList = []
personList.append(Person("Payne N. Diaz", "coach", "Without exception, there is no rule!"))
'''


f = open("alert.ids", "r")
searchstringsAttack = ('PingOfDeathDetected')


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
      EventsList[i].severity_level="low"
      #Insert To Data Base Event
      print( "IP-source: "+EventsList[i].ipSrc)
      print( "IP-destination: "+EventsList[i].ipDes)
      print( "Date_Time: "+EventsList[i].time)
      print( "severity_level: "+EventsList[i].severity_level)
      print( "begin in row number: "+EventsList[i].file_name_index)
      print( "summry: "+EventsList[i].summry)
      print( "============================================================================")
      
      
   elif( sourceMap.get(EventsList[i].keyinMap) <8) :
      EventsList[i].severity_level="medium"
      #Insert To Data Base Event
      print( "IP-source: "+EventsList[i].ipSrc)
      print( "IP-destination: "+EventsList[i].ipDes)
      print( "Date_Time: "+EventsList[i].time)
      print( "severity_level: "+EventsList[i].severity_level)
      print( "begin in row number: "+EventsList[i].file_name_index)
      print( "summry: "+EventsList[i].summry)
      print( "============================================================================")
   else:
      EventsList[i].severity_level="hight"
      #Insert To Data Base Event
      print( "IP-source: "+EventsList[i].ipSrc)
      print( "IP-destination: "+EventsList[i].ipDes)
      print( "Date_Time: "+EventsList[i].time)
      print( "severity_level: "+EventsList[i].severity_level)
      print( "begin in row number: "+EventsList[i].file_name_index)
      print( "summry: "+EventsList[i].summry)
      print( "============================================================================")
   i+=1
   
    


