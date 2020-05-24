import WindowsPlatform
import time
def getOneTimeInfo():
    sistem=WindowsPlatform.WindowsPlatform()
    info={}
    # info["cpuFreq"]=sistem.getCpuFreq()
    # info["cpuPhycalCores"]=sistem.physicalCores
    info["memoryInstaled"]=sistem.TotalMemory
    # info["totalCores"]=sistem.totalCores
    info["networkInfo"]=sistem.getNetworkInfo()
    info["diskInfo"]=sistem.getDiskInfo()
    return info
def getInfo():
    sistem = WindowsPlatform.WindowsPlatform()
    info = {}
    info["cpuTemp"] = sistem.getCpuTemp()
    info["memoryTemp"]=sistem.getMemoryTemp()
    info["memoryUsage"] = sistem.getMemoryUsage()
    info["fanSpeed"] = sistem.getFanSpeed()
    info["networkSpeed"] = sistem.getNetworkSpeed()
    time.sleep(1)
    info["cpuavgpercent"] = sistem.getAvgCpuPercent()

    return info

if __name__=="__main__":
    d=getOneTimeInfo()
    print(d)
    d=getInfo()
    print(d)