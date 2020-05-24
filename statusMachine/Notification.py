# Python code to illustrate Sending mail
# to multiple users
# from your Gmail account
import smtplib
import threading
import re
import sched, time
import Server
import detectOs
ALERT_WHEN_CPU_TEMP='95.0'
ALERT_WHEN_MEMORY_TEMP='95.0'
ALERT_WHEN_MEMORY_USAGE=95.0
ALERT_WHEN_FANSPEED1='5000'
ALERT_WHEN_FANSPEED2='5000'
ALERT_WHEN_DISK_PERCENTAGE=95.0
ALERT_WHEN_CPUAVGPERCENTAGE=100
MESAJ_CPUAVGPERCENTAGE="Temperatura tuturol procesoarelor este mai mult de 95%"
MESAJ_PERCENTAGE="Disk-ul este full la 95%"
MESAJ_CPU_TEMP="Procesorul este utilizat mai mult de 95%"
MESAJ_MEMORY_TEMP = "Temperatura memoriei este ridica peste 95%"
MESAJ_MEMORY_USAGE = "Memoria este utilizata la 95%"
MESAJ_FANSPEED1="Viteza cooler1 este foarte ridicata"
MESAJ_FANSPEED2="Viteza cooler2 este foarte ridicata"
MESAJ_APLICATION="Alerta Diogen, vedem daca o folosim"

MESAJ2=""
MESAJ=""
global ALERT_CPU_TEMP
global ALERT_MEMORY_TEMP
global ALERT_MEMORY_USAGE
global ALERT_FANSPEED1
global ALERT_FANSPEED2
global ALERT_DISK_PERCENTAGE
global ALERT_CPUAVGPERCENTAGE
ALERT_CPU_TEMP=False
ALERT_MEMORY_TEMP=False
ALERT_MEMORY_USAGE=False
ALERT_FANSPEED1=False
ALERT_FANSPEED2=False
ALERT_DISK_PERCENTAGE=False
ALERT_CPUAVGPERCENTAGE=False
OPTIMAL_CPU_TEMP='50.0'
OPTIMAL_MEMORY_TEMP='50.0'
OPTIMAL_MEMORY_USAGE=50.0
OPTIMAL_FANSPEED1='4500'
OPTIMAL_FANSPEED2='4500'
OPTIMAL_DISK_PERCENTAGE=50.0
OPTIMAL_CPUAVGPERCENTAGE=50.0
ALERT_SENT=False
regex = '[A-Z0-9a-z._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,5}'
list_of_users = []
global priorityList
priorityList=[]
class Notification:
    def __init__(self):
        self.cputemp=0
        self.memorytemp=0
        self.memoryusage=0
        self.fanspeed1=0
        self.fanspeed2=0
        self.dickpercentage=0
        self.cpuavgpercentage=0

    def updateValues(self,dic2,dic):
        self.cputemp=dic2['cpuTemp']['CpuAVG1']
        self.memorytemp=dic2['memoryTemp']['Memory0']
        self.memoryusage=dic2['memoryUsage']['MemoryPercent']
        self.fanspeed1=dic2['fanSpeed']['Fan0']
        self.fanspeed2=dic2['fanSpeed']['Fan1']
        self.dickpercentage=dic['diskInfo']['Disk0']['Percentage']
        self.cpuavgpercentage=dic2['cpuavgpercent']

    def selfCheck1(self):
        print(self.cputemp," ",self.cpuavgpercentage)
        global ALERT_DISK_PERCENTAGE,ALERT_CPU_TEMP,ALERT_MEMORY_TEMP,ALERT_MEMORY_USAGE,ALERT_FANSPEED1, ALERT_FANSPEED2,ALERT_CPUAVGPERCENTAGE,MESAJ,ALERT_SENT
        if self.dickpercentage >= ALERT_WHEN_DISK_PERCENTAGE and ALERT_DISK_PERCENTAGE == False:
            ALERT_DISK_PERCENTAGE = True
            MESAJ+=" - "+MESAJ_PERCENTAGE+";"+"\n"
        else:
            if (self.dickpercentage <= OPTIMAL_DISK_PERCENTAGE and ALERT_DISK_PERCENTAGE == True):
                ALERT_DISK_PERCENTAGE = False

        if  self.cputemp >= ALERT_WHEN_CPU_TEMP and ALERT_CPU_TEMP==False:
            MESAJ+=" - "+MESAJ_CPU_TEMP+";"+"\n"
            ALERT_CPU_TEMP=True
        else:
            if(self.cputemp<=OPTIMAL_CPU_TEMP and ALERT_CPU_TEMP==True):
                ALERT_CPU_TEMP=False

        if self.memorytemp >= ALERT_WHEN_MEMORY_TEMP and ALERT_MEMORY_TEMP==False:
           MESAJ+=" - "+MESAJ_MEMORY_TEMP+";"+"\n"
           ALERT_MEMORY_TEMP=True
        else:
            if (self.memorytemp<=OPTIMAL_MEMORY_TEMP and ALERT_MEMORY_TEMP==True):
               ALERT_MEMORY_TEMP=False

        if (self.memoryusage >=ALERT_WHEN_MEMORY_USAGE and ALERT_MEMORY_USAGE==False):
            MESAJ+=" - "+MESAJ_MEMORY_USAGE+";"+"\n"
            ALERT_MEMORY_USAGE=True
        else:
            if( self.memoryusage <=OPTIMAL_MEMORY_USAGE and  ALERT_MEMORY_USAGE==True):
                ALERT_MEMORY_USAGE=False
                ALERT_SENT = False

        if(self.fanspeed1>= ALERT_WHEN_FANSPEED1 and  ALERT_FANSPEED1==False):
            MESAJ+=" - "+MESAJ_FANSPEED1+";"+"\n"
            ALERT_FANSPEED1=True
        else:
            if(self.fanspeed1<=OPTIMAL_FANSPEED1 and  ALERT_FANSPEED1==True):
                ALERT_FANSPEED1=False

        if self.fanspeed2>= ALERT_WHEN_FANSPEED2 and  ALERT_FANSPEED2==False:
            MESAJ+=" - "+MESAJ_FANSPEED2+";"+"\n"
            ALERT_FANSPEED2= True
        else:
            if self.fanspeed2<=OPTIMAL_FANSPEED2 and  ALERT_FANSPEED2==True:
                ALERT_FANSPEED2=False

        if( self.cpuavgpercentage>ALERT_WHEN_CPUAVGPERCENTAGE and  ALERT_CPUAVGPERCENTAGE==False):
            MESAJ+=" - "+MESAJ_CPUAVGPERCENTAGE+";"+"\n"
            ALERT_CPUAVGPERCENTAGE=True
        else:
            if(self.cpuavgpercentage <OPTIMAL_CPUAVGPERCENTAGE and  ALERT_CPUAVGPERCENTAGE==True):
                ALERT_CPUAVGPERCENTAGE=False
        if len(MESAJ)>0:
            if(ALERT_SENT==False):
                self.sendAlert(list_of_users, MESAJ)
            MESAJ=""
        if ALERT_CPU_TEMP==False and ALERT_MEMORY_TEMP==False and ALERT_MEMORY_USAGE==False and ALERT_FANSPEED1==False and ALERT_FANSPEED2==False and ALERT_CPUAVGPERCENTAGE==False:
            ALERT_SENT=False

    def emailValidicion(self, email):
        if re.search(regex, email):
            return True
        else:
            return False
    def sendAlert(self,li, mesaj):
        global ALERT_SENT
        global MESAJ2
        ALERT_SENT = True
        for dest in li:
            if(Server.getUserPreferences(dest)==1):
                print("Sending... Alert!")
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login("serverhealth3@gmail.com", "cristidiogensergiu123@")
                name = re.split('[._]', dest)
                MESAJ2 += "Buna, " + name[0].capitalize() + "!\n"
                MESAJ2 += "Server-ul are urmatoarele probleme:"
                message = "\r\n".join([
                    "From: Server Health",
                    "To:" + dest,
                    "Subject: Alert!",
                    "", MESAJ2 + "\n" + mesaj

                ])
                s.sendmail("serverhealth3@gmail.com", dest, message)
                s.quit()
                print("Alert sent!")
                MESAJ2 = ""

    def addUsers(self,l):
        for i in l:
            if (self.emailValidicion(i)):
                list_of_users.append(i)
    def systemMonitoring(self):
        threading.Timer(10000,self.systemMonitoring).start()
        d1,d2=detectOs.getUpdateForNotification()
        self.updateValues(d1,d2)
        self.selfCheck1()


def notificatioMain():
    s = sched.scheduler(time.time, time.sleep)
    c1=Notification()
    global listlen
    listlen=0
    def verify(sc):
        lista_temp = Server.getListOfUsers()
        global listlen,priorityList
        if(len(lista_temp)>listlen):
            listlen+=1
            c1.addUsers(lista_temp)
        if(len(lista_temp)>0):
            c1.systemMonitoring()


        s.enter(2, 1, verify, (sc,))

    s.enter(2, 1, verify, (s,))
    s.run()
# if __name__=="__main__":
#     Server.main()
#     notificatioMain()