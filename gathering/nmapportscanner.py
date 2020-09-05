#
# This script was created by Sammwy for PenPy (Copyright 2020)
#   Twitter: @Sammwy
#   Github: https://github.com/sammwyy/PenPy
#

import nmap
import sys
import threading
import socket

# Check if script has the correct arguments
if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " <ip address/hostname>")
    sys.exit(1)

target = str(socket.gethostbyname(sys.argv[1]))
ports = [21, 22, 23, 25, 53, 80, 110, 115, 135, 139, 143, 194, 443, 445, 1433, 3306, 3389, 5631, 5900, 8080, 25565, 1]

# Banner
print("\nPenPy - PortScanner")
print("Analizing: " + sys.argv[1])
print("----------------------------")

# Instantiate scanner
scanner = nmap.PortScanner()

# Check and print if the host is up or down
portscan = scanner.scan(target, str(1))
data = portscan['scan'][target]

print("Host " + target + " is " + data['status']['state'])

# Stop script if the host is down
if portscan['scan'][target]['status']['state'] != "up":
    print("----------------------------")
    print("Finish! Thanks you for use PenPy\n")
    sys.exit(0)

# Show server info
print("Detected hostname for host: " + data["hostnames"][0]["name"])
print("Scanning for most commons ports...")


# Show message
print("----------------------------")

# Make this tool multi-thread
class scanThread (threading.Thread):
    def __init__ (self, port):
        threading.Thread.__init__(self)
        self.port = port

    def run (self):
        port = self.port
        portscan = scanner.scan(target, str(port))
        _scan = portscan['scan'][target]['tcp'][port]
        _status = _scan['state']

        ports.remove(port)

        if _status == "open":
            print("Port " + str(port) + " (" + _scan["name"] + ") is open and running " + ( _scan["product"] or "Unknown Service")  + " Version " + ( _scan["version"] or "N/A"))

        # Show end message when all ports is scanned
        if len(ports) == 0:
            print("----------------------------")
            print("Finish! Thanks you for use PenPy\n")

# Scann all ports in the array
for port in ports:
    thread = scanThread(port)
    try:
        thread.start()
    except:
        pass