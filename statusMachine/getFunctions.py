import subprocess
from time import sleep
def getFanSpeed():
    process = subprocess.Popen(["./SMC_LIBRARY", "f"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
    out, err = process.communicate()
    output=out.decode("utf-8")
    process.kill()
    process.terminate()
    output=output.split()
    dic={}
    for i in range(len(output)):
        dic[f"Fan{i}"]=output[i]
    return dic

def getCpuTemp():
    process = subprocess.Popen(["./SMC_LIBRARY", "a"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
    out, err = process.communicate()
    output = out.decode("utf-8")
    process.kill()
    process.terminate()
    output = output.split()
    dic = {}
    for i in range(len(output)):
        dic[f"CpuTemp{i+1}"] = output[i]
    return dic
def getCPUAVG():
    process = subprocess.Popen(["./SMC_LIBRARY", "c"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
    out, err = process.communicate()
    output = out.decode("utf-8")
    process.kill()
    process.terminate()
    output = output.split()
    dic = {}
    for i in range(len(output)):
        dic[f"CpuAVG{i + 1}"] = output[i]
    return dic
def getMemoriTemp():
    process = subprocess.Popen(["./SMC_LIBRARY", "m"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
    out, err = process.communicate()
    output = out.decode("utf-8")
    process.kill()
    process.terminate()
    output = output.split()
    dic = {}
    for i in range(len(output)):
        dic[f"Memory{i}"] = output[i]
    return dic
