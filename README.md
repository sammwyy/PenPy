<img src="https://raw.githubusercontent.com/sammwyy/PenPy/master/assets/pentest.svg" width="128px" align="left">
<h1>PenPy</h1>
<p>A toolkit for pentesting in python <br/>
Donate to the project in <a href="https://paypal.me/sammwy">Paypal</a>, in <a href="https://ko-fi.com/sammwy">Ko-fi</a> or in <a href="https://patreon.com/sammwy">Patreon</a></p>

## 🔰 Index
- [🔍 Gathering](#gathering)
  - [🦄 HTTP Lookup](#🦄-http-lookup)
  - [🐱 IP Lookup](#🐱-ip-lookup)
  - [🐗 Nmap Port Scaner](#🐗-nmap-port-scanner)
  - [🐘 Recon](#🐘-recon)
  - [🐨 Subdomain Fuzzer](#🐨-subdomain-fuzzer)

## 🔍 Gathering
#### 🦄 HTTP Lookup  
This script makes an HTTP request and downloads the headers to check if the connection is secure.  
[httplookup.py](https://github.com/sammwyy/PenPy/blob/master/gathering/httplookup.py)  

#### 🐱 IP Lookup 
This script makes use of an api to resolve the data of an IP such as coordinates, hostname and geolocation.  
[iplookup.py](https://github.com/sammwyy/PenPy/blob/master/gathering/iplookup.py)  

#### 🐗 Nmap Port Scanner
This script makes use of the NMAP tool to scan ports in a multi-threaded way. It is also able to show the service and version that the port is running.  
[nmapportscanner.py](https://github.com/sammwyy/PenPy/blob/master/gathering/nmapportscanner.py)  

#### 🐘 Recon
This script runs HTTP Lookup and IP Lookup.  
[recon.py](https://github.com/sammwyy/PenPy/blob/master/gathering/recon.py)

#### 🐨 Subdomain Fuzzer
This script uses a [Dictionary](https://github.com/sammwyy/PenPy/blob/master/data/subdomains.txt) to discover subdomains.  
[subdomains.p](https://github.com/sammwyy/PenPy/blob/master/gathering/subdomains.py)
