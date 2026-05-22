from scanner.subnet_scanner import scan_subnet
from scanner.port_checker import check_ports

live_hosts = scan_subnet("192.168.1")

for host in live_hosts:
    check_ports(host)
