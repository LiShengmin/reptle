import urllib
url ="http://192.240.120.108//mp43/228798.mp4"
name = "银行职员的诱惑.mp4"
print 'loading'
urllib.urlretrieve(url, name) 
print 'finish'