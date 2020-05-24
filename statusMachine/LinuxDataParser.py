import LinuxPlatform
import time
def getOneTimeInfo():
    sistem=LinuxPlatform.LinuxPlatform()
    info={}
    #info["cpuFreq"]=sistem.getCpuFreq()
    #info["cpuPhycalCores"]=sistem.physicalCores
    info["memoryInstaled"]=sistem.TotalMemory
    #info["totalCores"]=sistem.totalCores
    info["networkInfo"]=sistem.getNetworkInfo()
    info["diskInfo"]=sistem.getDiskInfo()
    return info
def getInfo():
    sistem = LinuxPlatform.LinuxPlatform()
    info = {}
    info["cpuTemp"] = sistem.getCpuTemp()
    info["memoryUsage"] = sistem.getMemoryUsage()
    info["fanSpeed"] = sistem.getFanSpeed()
    info["networkSpeed"] = sistem.getNetworkSpeed()
    info["cpuCorePercent"] = sistem.getCpuCorePercent()

    return info