import OsxPlatform
import time
def getOneTimeInfo():
    sistem=OsxPlatform.OsxPlatfrom()
    info={}
    #info["cpuFreq"]=sistem.getCpuFreq()
    #info["cpuPhycalCores"]=sistem.physicalCores
    info["memoryInstaled"]=sistem.TotalMemory
    #info["totalCores"]=sistem.totalCores
    info["networkInfo"]=sistem.getNetworkInfo()
    info["diskInfo"]=sistem.getDiskInfo()
    return info
def getInfo():
    sistem = OsxPlatform.OsxPlatfrom()
    info = {}
    info["cpuTemp"] = sistem.getAvgCpuTemp()
    info["memoryTemp"] = sistem.getMemoryTemp()
    info["memoryUsage"] = sistem.getMemoryUsage()
    info["fanSpeed"] = sistem.getFanSpeed()
    info["networkSpeed"] = sistem.getNetworkSpeed()
    # info["cpuCorePercent"] = sistem.getCpuCorePercent()
    info["cpuavgpercent"]=sistem.getAvgCpuPercent()
    return info

if __name__=="__main__":
    data=getOneTimeInfo()
    print(data['networkInfo']['AF_INET1']['IP Address'])
