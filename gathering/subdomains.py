#
# This script was created by Sammwy for PenPy (Copyright 2020)
#   Twitter: @Sammwy
#   Github: https://github.com/sammwyy/PenPy
#

import socket
import sys
import threading

# Check if script has the correct arguments
if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " <domain>")
    sys.exit(1)

# Open subdomain list
file = open("data/subdomains.txt").read()
subdomains = file.splitlines()

# Banner
print("\nPenPy - Subdomain Fuzzer")
print("Analizing: " + sys.argv[1])
print("----------------------------")
print("Subdomains loaded in list: " + str(len(subdomains)))
print("----------------------------")


# Iterate subdomain list
for sd in subdomains:
    # Try resolve subdomain
    try:
        name = sd + "." + sys.argv[1]
        ip = socket.gethostbyname(name)

    # If it not responds, ignore.
    except:
        subdomains.remove(sd)
        pass

    # Else show a message
    else:
        subdomains.remove(sd)
        print( "Subdomain \"" + sd + "\" with ip (" + ip + ") discovered in: " + sys.argv[1])

        if len(subdomains) == 0:
            print("----------------------------")
            print("Finish! Thanks you for use PenPy\n")

     