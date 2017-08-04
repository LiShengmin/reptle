import urllib2, re, requests, BeautifulSoup
from lxml import etree

header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
            , "Connection": "keep-alive"
         }
base = 'http://t66y.com/htm_data/22/1707/2533995.html'
base2 = 'http://www.baidu.com'

req = urllib2.Request(base, headers = header)
print 'open'
try:
    rep = urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print e.code
    print e.reason
    print e.geturl()
    print e.read()
    pass
print 'data'
htmldata = html.read()

print hemldata
titles = html.xpath('//video[@class="fp-engine"]/@src')

downURL = 'http://www.ri003.com/get_file/3/595c9ba3880ef2d4fafa0ee3ab9e48bb/39000/39283/39283.mp4/'
print titles


