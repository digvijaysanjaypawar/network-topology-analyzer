import subprocess
import platform

def ping_host(ip):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", ip]
    result = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if result.returncode == 0:
        print(f"{ip} is up")
    else:
        print(f"{ip} is down")

ping_host("8.8.8.8")
ping_host("192.168.1.1")            
