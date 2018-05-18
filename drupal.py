#!/usr/bin/env python
import version
import sys,argparse,os
import requests
from random import randint
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

target = raw_input(bcolors.OKGREEN + "Target :" + bcolors.ENDC)
yn = raw_input(bcolors.WARNING + "Do you want use proxy ?"+ bcolors.BOLD +"[Y/N] :" + bcolors.ENDC)
if yn == "Y":
	p_ip = raw_input(bcolors.OKGREEN + "IP :" + bcolors.ENDC)
	p_port = raw_input(bcolors.OKGREEN + "PORT :" + bcolors.ENDC)
	p_full = p_ip + ":" + p_port
else:
	p_full = "138.201.223.250:31288"

http_proxy = p_full


proxyDict = {"http":http_proxy}

hostsearch = "http://api.hackertarget.com/hostsearch/?q=" + target

response = requests.get(hostsearch, headers={'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13'},proxies=proxyDict)

hosts_ips = response.text


content = hosts_ips.split("\n")

result = []

for line in content:

        result.append(line.split(',')[0])

for host in result:
	print version.get_version("http://"+ host + "/CHANGELOG.txt")


