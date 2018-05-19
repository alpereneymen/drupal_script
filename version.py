import requests,re
def get_version(url):
	p_full = "138.201.223.250:31288"
	http_proxy = p_full


	proxyDict = {"http":http_proxy}

	hostsearch = url
	response = requests.get(hostsearch, headers={'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13'},proxies=proxyDict)

	contents = response.text
	splitted = contents.split()
	print "[+]"+ url +" Version : " + splitted[1]




