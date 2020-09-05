#
# This script was created by Sammwy for PenPy (Copyright 2020)
#   Twitter: @Sammwy
#   Github: https://github.com/sammwyy/PenPy
#

import sys
import requests
import socket
import json

# Check if script has the correct arguments
if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " <ip address>")
    sys.exit(1)

# Banner
print("\nPenPy - IP Lookup")
print("Analizing: " + sys.argv[1])
print("----------------------------")

# Request to ipinfo.io
ip_address = socket.gethostbyname(sys.argv[1])
ipinfo_req = requests.get("https://ipinfo.io/" + ip_address + "/json")
ipinfo_res = json.loads(ipinfo_req.text)

# Print results
print("IP Address: " + ip_address)
print("Location: " + ipinfo_res['loc'])
print("Region: " + ipinfo_res["region"])
print("City: " + ipinfo_res["city"])
print("Country: " + ipinfo_res["country"])
print("----------------------------")

# Finish message
print("Finish! Thanks you for use PenPy\n")