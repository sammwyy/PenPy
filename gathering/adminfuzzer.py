#
# This script was created by Sammwy for PenPy (Copyright 2020)
#   Twitter: @Sammwy
#   Github: https://github.com/sammwyy/PenPy
#

import sys
import requests
import threading
import json
import ssl

# Check if script has the correct arguments
if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " <url>")
    sys.exit(1)

# Banner
print("\nPenPy - Admin Fuzzer")
print("Analizing: " + sys.argv[1])

# Make test requests for handle 404
scan_mode = ""
body404 = ""

baseurl = "https://" + sys.argv[1]
req = requests.get(baseurl + "/0xSk1A_xD4lfV4kaXlaW301ClaXdleobF021XalcoeA")

status = req.status_code

if status == 404:
    scan_mode = "STATUS_404"
elif "404" in str(req.content):
    scan_mode = "WORD_404"
else:
    scan_mode = "BODY_404"
    body404 = str(req.content)

# Open urls list
file = open("data/admin.txt").read()
urls = file.splitlines()

# Show dictionary length
print("----------------------------")
print("Admin Urls loaded in list: " + str(len(urls)))
print("----------------------------")

# Make this tool multi-thread
class scanThread (threading.Thread):
    def __init__ (self, url):
        threading.Thread.__init__(self)
        self.url = url
    
    def run (self):
        url = self.url
        if url.startswith("/"):
            url = baseurl + url
        else:
            url = baseurl + "/" + url

        url_req = requests.get(url)

        if scan_mode == "STATUS_404":
            if url_req.status_code != 404:
                print("Discovered url " + url)
        elif scan_mode == "WORD_404":
            if "404" in str(url_req.content):
                pass
            else:
                print("Discovered url " + url)
        elif scan_mode == "BODY_404":
            if str(url_req.content) != body404:
                print("Discovered url " + url)

# Launch scan
for url in urls:
    thread = scanThread(url)
    try:
        thread.start()
    except:
        pass