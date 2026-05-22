import csv
import json
from datetime import datetime

def save_report(scan_results):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    # Save CSV
    csv_file = f"network_report_{timestamp}.csv"
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['IP Address', 'Status', 'Port', 'Service', 'Port Status'])
        for entry in scan_results:
            for port_info in entry['ports']:
                writer.writerow([
                    entry['ip'],
                    entry['status'],
                    port_info['port'],
                    port_info['service'],
                    port_info['state']
                ])
    print(f"CSV report saved: {csv_file}")

    # Save JSON
    json_file = f"network_report_{timestamp}.json"
    with open(json_file, 'w') as f:
        json.dump(scan_results, f, indent=4)
    print(f"JSON report saved: {json_file}")

# Test data
results = [
    {
        "ip": "192.168.1.1",
        "status": "UP",
        "ports": [
            {"port": 22,  "service": "SSH",   "state": "CLOSED"},
            {"port": 23,  "service": "Telnet","state": "CLOSED"},
            {"port": 80,  "service": "HTTP",  "state": "OPEN"},
            {"port": 443, "service": "HTTPS", "state": "CLOSED"}
        ]
    },
    {
        "ip": "8.8.8.8",
        "status": "UP",
        "ports": [
            {"port": 22,  "service": "SSH",   "state": "CLOSED"},
            {"port": 23,  "service": "Telnet","state": "CLOSED"},
            {"port": 80,  "service": "HTTP",  "state": "CLOSED"},
            {"port": 443, "service": "HTTPS", "state": "CLOSED"}
        ]
    }
]

save_report(results)