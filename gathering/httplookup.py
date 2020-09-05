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
    print("Usage: " + sys.argv[0] + " <url>")
    sys.exit(1)

# Banner
print("\nPenPy - HTTP Lookup")
print("Analizing: " + sys.argv[1])

# Headers Lookup
req = requests.get("https://" + sys.argv[1])
headers = req.headers

print("----------------------------")
cache_control = "<none>"
content_type = "<none>"
csp = "<none>"
content_encoding = "<none>"
hsts = False
x_content_type = "<none>"
x_frame = "<none>"
x_powered = "<none>"
x_xss = "<none>"

if "Cache-Control" in headers:
    cache_control = headers["Cache-Control"]
if "Content-Type" in headers:
    content_type = headers["Content-Type"]
if "content-security-policy" in headers:
    csp = "YES"
if "Content-Encoding" in headers:
    content_encoding = headers["Content-Encoding"]
if "strict-transport-security" in headers:
    hsts = True
if "x-content-type-options" in headers:
    x_content_type = headers["x-content-type-options"]
if "X-Frame-Options" in headers:
    x_frame = headers["X-Frame-Options"]
if "x-powered-by" in headers:
    x_powered = headers["x-powered-by"]
if "X-XSS-Protection" in headers:
    x_xss = headers["X-XSS-Protection"]

print("Cache Control: " + cache_control)
print("Content Type: " + content_type)
print("CSP: " + csp)
print("Content Encoding: " + content_encoding)
print("HSTS: " + str(hsts))
print("X-Content-Type-Options: " + x_content_type)
print("X-Frame-Options: " + x_frame)
print("X-Powered-By: " + x_powered)
print("X-XSS Protection: " + x_xss)

print("----------------------------")

# Cookies Check
cookie_str = ""
cookies_use = False

if "Set-Cookie" in headers:
    cookie_str = headers["Set-Cookie"].lower()
    cookies_use = True

cookies_secure = "secure" in cookie_str
cookies_httponly = "httponly" in cookie_str

print("Cookie enabled: " + str(cookies_use))
print("Cookie secure: " + str(cookies_secure))
print("Cookie httponly: " + str(cookies_httponly))

print("----------------------------")
print("Finish! Thanks you for use PenPy\n")