import subprocess

def getCpuTemp():
    psscript = """
    CLS
    Add-Type -Path "library/OpenHardwareMonitorLib.dll"
    $Comp = New-Object -TypeName OpenHardwareMonitor.Hardware.Computer
    $Comp.Open()
    $Comp.CPUEnabled = $true
    $Comp.MainboardEnabled = $true
    $Comp.FanControllerEnabled = $true
    ForEach ($HW in $Comp.Hardware) {
    $HW.Update()
        If ( $hw.HardwareType -eq "CPU"){
            ForEach ($Sensor in $HW.Sensors) {
            If ($Sensor.SensorType -eq "Temperature"){       
    $Sensor.Value.ToString() 
            }                                                                                                                                                                                                          
        
    }
    
    $Comp.Close()}}
    """

    si = subprocess.STARTUPINFO()
    si.dwFlags |= subprocess.STARTF_USESHOWWINDOW

    cmd = ['powershell.exe', '-Command',  psscript]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, startupinfo=si)
    tmp = proc.stdout.readline()

    tmp=tmp.decode("utf-8")
    temperature=float(tmp)
    temperature=str(temperature)
    return temperature
if __name__=="__main__":
    a=getCpuTemp()
    print(type(a))
    print(a)