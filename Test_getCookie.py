import sys
import requests


def getCookie(url):
    cookie = cookielib.CookieJar()
    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(handler)
    urllib2.install_opener(opener)

    response = opener.open(url)
    print ''
    print cookie
    print url

    for item in cookie:
        print item.name + '    :      ' + item.value

getCookie('http://www.zngirls.com/g/23209')

getCookie('http://www.baidu.com')



request = urllib2.Request("http://www.zngirls.com/g/23209")
opener = urllib2.build_opener(urllib2.HTTPHandler(debuglevel=1))#为了开启回显，需要手动构造一个HTTPHandler
feeddata = opener.open(request).read()
