import subprocess
import platform
def ping_host(ip):
    param ='-n' if platform.system().lower()=='windows' else '-c'
    command=('ping', param, '1','-w','500', ip)
    result=subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return result.returncode == 0
def scan_subnet(base_ip):
    print(f"Scanning network: {base_ip}.0/24")
    print("_"*40)
    live_hosts = []
    for i in range(1, 255):
        ip = f"{base_ip}.{i}"
        if ping_host(ip):
            print(f"(up) {ip}")
            live_hosts.append(ip)
        else:
            print(f"(down) {ip}")
    print("_"*40)
    print(f"scan complete. {len(live_hosts)} hosts found alive.")
    return live_hosts

if __name__ == '__main__':
    scan_subnet("192.168.1")
