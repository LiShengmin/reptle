#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests, re, urllib, urllib2, string, os
from lxml import etree

baseUrl = "http://www.budejie.com/video/"
res = requests.get(baseUrl).text
print "url:", baseUrl, '下载器\n\n'

html = etree.HTML(res)
titles = html.xpath('//div[@class="j-r-list-tool"]/@data-title')

def stringNoCarle(self):#规则化name
    name = self
    string = re.sub("[\~\“\”《》\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+".decode("utf8"), "_".decode("utf8"), name)  
    if string[-1] == '_':#最后一个字符不是_
        string = string[0:len(string)-1]
    return string


def isHaveInOS(name):
    path = "/Users/lishengmin/Desktop/Python/"
    tempname = ""
    if len(tempname) < 3:
            n = name.encode('utf8')
            tempname = "{0}".format(n)
    for dir in os.listdir(path):
        if dir == tempname :
            return True
    return False

re_url = r'href="(.*?).mp4"'
urls = re.findall(re_url, res)

index = 0
for u in urls :
    url = u+".mp4"
    title = titles[index]
    title = stringNoCarle(title)
    name = title+".mp4"
    isbeing = isHaveInOS(name)

    if isbeing:
        print name,"文件已存在"
        pass
    else:
        print name, "Download"
        urllib.urlretrieve(url, name)    #这句话是下载的，如果不开下载测试的化不用这句话
        print 'done!!', url, '\n'
        pass
    index +=1

print "finish"


