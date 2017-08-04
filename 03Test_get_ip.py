# -*- coding: UTF-8 -*-  
# SyntaxError: Non-ASCII character '\xe5' in file /Users/lishengmin/Desktop/Python/Test_get_ip.py on line 2, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details


# import socket
# localIP = socket.gethostbyname(socket.gethostname())#得到本地ip
# print "local ip:%s "%localIP
 
# ipList = socket.gethostbyname_ex(socket.gethostname())
# for i in ipList:
#     if i != localIP:
#        print "external IP:%s"%i


#通过本地链接获取ip
import socket

def get_lan_ip():
#  '''
#  Returns the actual ip of the local machine.
#  This code figures out what source address would be used if some traffic
#  were to be sent out to some well known address on the Internet. In this
#  case, a Google DNS server is used, but the specific address does not
#  matter much. No traffic is actually sent.
#  '''
    try:
        csock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        csock.connect(('8.8.8.8', 80))
        (addr, port) = csock.getsockname()
        csock.close()
        return addr
    except socket.error:
        return "127.0.0.1"

# 通过网站获取 ip
import re,urllib2
from xml import etree
def get_local_ip():
    try:
        myip = visit("http://www.ip138.com/ip2city.asp")
    except:
        try:
            myip = visit("http://www.bliao.com/ip.phtml")
        except:
            try:
                myip = visit("http://www.whereismyip.com/")
            except:
                myip = "So sorry!!!"
    return myip

def visit(url):
    opener = urllib2.urlopen(url)
    html_data = opener.read()
    ip = re.findall('[0-9]+.[0-9]+.[0-9]+.[0-9]+', html_data)[0]
    return ip

#ip转换经纬度
from geoip import geolite2
def get_location(addressIP):
    line = geolite2.lookup(addressIP)
    return line.location



if __name__ == "__main__":
     lanIP = get_lan_ip() 
     print lanIP
     localip = get_local_ip()
     print localip
     location = get_location(localip)
     print location[0] 
     print location[1]
