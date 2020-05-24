import platform
import OsxDataParser
import LinuxDataParser
import WindowsDataParser

def detectPlatform(repeat):
    plat=platform.system()
    if(plat=="Darwin"):
        if repeat==False:
            return OsxDataParser.getOneTimeInfo()
        if repeat==True:
            return OsxDataParser.getInfo()

    if(plat=="Linux"):
        if repeat==False:

            return LinuxDataParser.getOneTimeInfo()
        if repeat==True:
            return LinuxDataParser.getInfo()


    if(plat=="Windows"):
        if repeat==False:
            return WindowsDataParser.getOneTimeInfo()
        if repeat==True:
            return WindowsDataParser.getInfo()
    else:
        print("Platform not suported!")
def getUpdateForNotification():
    plat = platform.system()
    if (plat == "Darwin"):
        return OsxDataParser.getInfo(),OsxDataParser.getOneTimeInfo()


    if (plat == "Linux"):
       return LinuxDataParser.getInfo(),LinuxDataParser.getOneTimeInfo()

    if (plat == "Windows"):
        return WindowsDataParser.getInfo(),WindowsDataParser.getOneTimeInfo()
    else:
        print("Platform not suported!")
def getIpAssigment():
    plat = platform.system()

    if (plat == "Darwin"):

        data=OsxDataParser.getOneTimeInfo()
        ip=data['networkInfo']['AF_INET1']['IP Address']
        return ip


    if (plat == "Linux"):
        data = LinuxDataParser.getOneTimeInfo()
        ip = data['networkInfo']['AF_INET1']['IP Address']
        return ip

    if (plat == "Windows"):

        data = WindowsDataParser.getOneTimeInfo()
        ip = data['networkInfo']['AF_INET1']['IP Address']
        return ip

    else:
        print("Platform not suported!")

if __name__=="__main__":
    a=detectPlatform(False)
    print(a)