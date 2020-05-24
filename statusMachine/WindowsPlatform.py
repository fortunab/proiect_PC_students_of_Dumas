import psutil
import Cpu
import Fan
import time
def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

class WindowsPlatform:
    def __init__(self,perCPU=True,):
        self.physicalCores=psutil.cpu_count(logical=False)
        self.totalCores=psutil.cpu_count(logical=True)
        self.cpufreq = psutil.cpu_freq().current
        self.FanSpeed=str(Fan.getFanSpeed())
        self.CpuTemp=Cpu.getCpuTemp()
        # self.AvgCpuTemp=function.getCPUAVG()
        self.MemoryTemp='0'
        self.CpuCorePercent=self.getCpuCorePercent(perCPU)
        self.TotalMemory=self.getTotalMemory()

    def getCpuFreq(self):
        return self.cpufreq

    def getFanSpeed(self):
        Fan={"Fan0":self.FanSpeed,"Fan1":'0'}
        return Fan
    #
    def getAvgCpuPercent(self):
        val=0;
        nr=0;
        for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
            val += percentage
            nr=i
        time.sleep(0.1)
        val=val/nr
        if(val==100):
            return 100;
        else:
            val=round(val,2)
            return val
    def getCpuTemp(self):
        cpuTemp={'CpuAVG1':self.CpuTemp}
        return cpuTemp
    def getMemoryTemp(self):
        memoryTemp = {'Memory0': self.MemoryTemp}
        return memoryTemp
    def getCpuCorePercent(self, perCPU=True):
        dic = {}
        for i, percentage in enumerate(psutil.cpu_percent(percpu=perCPU)):
            dic[f"Core{i}"] = percentage
        return dic

    def getCoresPercent(self):
        return self.CpuCorePercent

    def getTotalMemory(self):
        svmem = psutil.virtual_memory()

        return get_size(svmem.total)

    def getMemoryUsage(self):
        dic = {}
        svmem = psutil.virtual_memory()
        dic["MemoryAvailable"] = get_size(svmem.available)
        dic["MemoryUsed"] = get_size(svmem.used)
        dic["MemoryPercent"] = svmem.percent
        return dic

    def getDiskInfo(self):
        dic = {}
        diskInfo = {}
        partitions = psutil.disk_partitions()
        i = 0
        for partition in partitions:
            diskInfo["FileSistem"] = partition.fstype
            diskInfo["Mountpoint"] = partition.mountpoint
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
            except PermissionError:

                continue

            diskInfo["Total Size"] = get_size(partition_usage.total)
            diskInfo["Used"] = get_size(partition_usage.used)
            diskInfo["Free"] = get_size(partition_usage.free)
            diskInfo["Percentage"] = partition_usage.percent
            dic[f"Disk{i}"] = diskInfo
            i += 1
        return dic

    def getNetworkInfo(self):
        interface = {}
        modules = {}
        modules2 = {}
        i = 0
        j = 0
        if_addrs = psutil.net_if_addrs()
        for interface_name, interface_addresses in if_addrs.items():
            for address in interface_addresses:
                if str(address.family) == 'AddressFamily.AF_INET':
                    modules["IP Address"] = address.address
                    modules["Netmask"] = address.netmask
                    modules["Broadcast IP"] = address.broadcast
                    interface[f"AF_INET{i}"] = modules
                    modules = {}
                    i += 1

                elif str(address.family) == 'AddressFamily.AF_PACKET':

                    modules2["MAC Address"] = address.address
                    modules2["Netmask"] = address.netmask
                    modules2["Broadcast MAC"] = address.broadcast
                    interface[f"AF_PACKET{j}"] = modules2
                    modules2 = {}
                    j += 1

        return interface

    def getNetworkSpeed(self):
        net_io = psutil.net_io_counters()
        speed = {}
        speed["Send speed"] = get_size(net_io.bytes_sent)
        speed["Recive speed"] = get_size(net_io.bytes_recv)
        return speed
if __name__=="__main__":
    a=WindowsPlatform()
    print(a.getNetworkSpeed())