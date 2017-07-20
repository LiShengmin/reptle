
#!/usr/bin/env python
# -*-coding:utf-8-*-
import  urllib2
from lxml import etree
from os import system
import requests
"""
第一步: 从 http://www.zngirls.com/rank/sum/ 开始抓取MM点击头像的链接(注意是分页的)
#第二部  http://www.zngirls.com/girl/21751/ 抓取每一个写真集合的链接(注意是分页的)
#第三部 http://www.zngirls.com/g/19671/1.html 在写真图片的具体页面抓取图片(注意是分页的)
"""
pciturelist=[]

header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
            , "Connection": "keep-alive"
         }

"""
从起始页面 http://www.zngirls.com/rank/sum/ 开始获取排名的页数和每一页的url
"""
def  mmRankSum():
    req = urllib2.Request("http://www.zngirls.com/rank/sum/", headers=header)
    html = urllib2.urlopen(req)
    htmldata = html.read()
    htmlpath = etree.HTML(htmldata)
    
    #首先获取页码数,然后用循环的方式挨个解析每一个页面
    pages = htmlpath.xpath('//div[@class="pagesYY"]/div/a/@href')


    for i in range( len(pages) -2 ):

        pagesitem="http://www.zngirls.com/rank/sum/"+ pages[i]
        mmRankitem(pagesitem)

"""
参数 url : 分页中每一页的具体url地址
通过穿过来的参数，使用  lxml和xpath 解析 html，获取每一个MM写真专辑页面的url
"""
def mmRankitem(url):
    req = urllib2.Request(url, headers=header)
    html = urllib2.urlopen(req)
    htmldata = html.read()
    htmlpath = etree.HTML(htmldata)

    pages = htmlpath.xpath('//div[@class="rankli_imgdiv"]/a/@href')
    for i in range(len(pages)):
       print  "http://www.zngirls.com/" + pages[i]+"album/"
       getAlbums("http://www.zngirls.com/" + pages[i]+"/album/")
       #print "http://www.zngirls.com/" + pages[i]


"""
参数 url : 每一个MM专辑的页面地址
通过穿过来的参数，获取每一个MM写真专辑图片集合的地址
"""
def getAlbums(girlUrl):
    req = urllib2.Request(girlUrl, headers=header)
    html = urllib2.urlopen(req)
    htmldata = html.read()
    htmlpath = etree.HTML(htmldata)
#    print 'FFFFF, girlURL'+girlUrl
    pages = htmlpath.xpath('//div[@class="igalleryli_div"]/a/@href')
    for i in range(len(pages)):
        getPagePicturess("http://www.zngirls.com/" + pages[i])

def getCookie(url):
    cookie = cookielib.CookieJar()
    #利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
    handler = urllib2.HTTPCookieProcessor(cookie)
    #通过handler来构建opener
    opener = urllib2.build_opener(handler)
    #此处的open方法同urllib2的urlopen方法，也可以传入request
    response = opener.open(url)
    for item in cookie:
        print 'Name = '+item.name
        print 'Value = '+item.value
    return cookie

"""
参数 url : 每一个MM写真专辑图片集合的地址
通过穿过来的参数，首先先获取图片集合的页数，然后每一页解析写真图片的真实地址
"""
def getPagePicturess(albumsurl):
    req = urllib2.Request(albumsurl, headers=header)
    html = urllib2.urlopen(req)
    htmldata = html.read()
    htmlpath = etree.HTML(htmldata)
    pages = htmlpath.xpath('//div[@id="pages"]/a/@href')

    for i in range(len(pages)-2):
        savePictures("http://www.zngirls.com" + pages[i])

"""
参数 url : 每一个MM写真专辑图片集合的地址(进过分页检测)
通过穿过来的参数，直接解析页面，获取写真图片的地址，然后下载保存到本地。
"""
def savePictures(itemPagesurl):

    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
        , "Connection": "keep-alive"
        , "Referer": "image / webp, image / *, * / *;q = 0.8"
        , "Accept":"image/webp,image/*,*/*;q=0.8"
    }
    try:
        req = urllib2.Request(itemPagesurl, headers=header)
        html = urllib2.urlopen(req)
        htmldata = html.read()
        htmlpath = etree.HTML(htmldata)
        print 'pageURL:' + itemPagesurl
        pages = htmlpath.xpath('//div[@class="gallery_wrapper"]/ul/img/@src')
        names = htmlpath.xpath('//div[@class="gallery_wrapper"]/ul/img/@alt')
    except Exception:
        pass
    for i in range(len(pages) ):
        print pages[i]
        # dowmImageURL = pages[i]
        # if dowmImageURL[8:2] != "ti":
        #     return
        # https://www.nvshens.com/g/23280/
        pciturelist.append(pages[i])
        referer = 'https://www.nvshens.com/g'+itemPagesurl[-6:]
        print 'referer:'+referer
        try:
            headers = {
                'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
                'Accept':'image/webp,image/apng,image/*,*/*;q=0.8',
                'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                'Accept-Language':"zh-CN,zh;q=0.8",
                'Accept-Encoding':'gzip, deflate, br',
                'Connection':'keep-alive',
                'Host':'t1.onvshen.com:85',
                'If-Modified-Since':'Fri, 14 Jul 2017 14:02:51 GMT',
                'If-None-Match':'cc56b1e1a9fcd21:0',
                "Referer": referer,
                "Referer-Address":"60.190.114.199:85",
                "Referrer-Policy":"no-referrer-when-downgrade",
            }
            req = urllib2.Request(pages[i], headers=headers)
            urlhtml = urllib2.urlopen(req)
            respHtml = urlhtml.read()

            binfile = open('MMPictrue/%s.jpg' % ( names[i] ) , "wb")
            print "name:"+ names[i]
            binfile.write(respHtml)
            binfile.close()
        except Exception :
            pass





mmRankSum()
"""
fl=open('list.txt', 'w')
for i in pciturelist:
    fl.write(i)
    fl.write("\n")
fl.close()
print '关机ing'
"""
print 'finish'
system('shutdown -s')