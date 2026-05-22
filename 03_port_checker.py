import socket

def check_ports(ip):
    ports = {
        22: 'SSH',
        23: 'Telnet',
        80: 'HTTP',
        443: 'HTTPS',
    }

    print(f"\nChecking ports on {ip}")
    print("-" * 40)

    for port, service in ports.items():
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)

            result = sock.connect_ex((ip, port))

            if result == 0:
                print(f"Port {port} ({service}) is OPEN")
            else:
                print(f"Port {port} ({service}) is CLOSED")

            sock.close()

        except Exception as e:
            print(f"Error checking port {port}: {e}")


# Call the function
target = input("Enter IP address: ")
check_ports(target)
