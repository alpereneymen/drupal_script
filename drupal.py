#!/usr/bin/env python

import sys,argparse,os,requests,re,random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

############################### GET VERSION FUNCTION
def get_version(url):

	


	hostsearch = url
	try:
	  	response = requests.get(hostsearch,timeout=5,headers={'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13'})

		

		contents = response.text
		
		if "Drupal" in contents:	
			splitted = contents.split()
			print "[+]"+ url +" Version : " + splitted[1]
		else:
			print "[-] It is not Drupal"
	except requests.ConnectionError:
		print "[-] Connection Failed !"
########################### GET VERSION FUNCTION
target = raw_input(bcolors.OKGREEN + "Target :" + bcolors.ENDC)
yn = raw_input(bcolors.WARNING + "Do you want use proxy ?"+ bcolors.BOLD +"[Y/N] :" + bcolors.ENDC)
if yn == "Y":
	p_ip = raw_input(bcolors.OKGREEN + "IP :" + bcolors.ENDC)
	p_port = raw_input(bcolors.OKGREEN + "PORT :" + bcolors.ENDC)
	p_full = p_ip + ":" + p_port
else:
	p_full = "181.196.145.106:65103"

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
	print ("http://"+ host + "/CHANGELOG.txt")

	get_version("http://"+ host + "/CHANGELOG.txt")
