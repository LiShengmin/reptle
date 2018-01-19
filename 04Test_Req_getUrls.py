
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import urllib2, re
# from lxml import etree

# 这是一个爬虫爬取 某个站所有URL的。 欢迎大家提iccess

# baseURL =  'https://www.nvshens.com'
baseURL =  "http://www.avtb009.com"
header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
            , "Connection": "keep-alive"
         }

'''
处理url的类，对已访问过的和未访问过的进行记录，待后续使用
'''
class linkQuence:

    def __init__(self):
        self.visited_urls = [] 
        self.unvisited_urls = []

    def get_visited_list(self):
        return self.visited_urls

    def get_unvisited_list(self):
        return self.unvisited_urls
    
    def isHave(self, new_url):
        for url in self.visited_urls:
            if url == new_url:
                return None
        for url in self.unvisited_urls:
            if url == new_url:
                return None
        return new_url

    def add_visited_list(self, new_url):
        new_url = self.isHave(new_url)
        if new_url is None:
            return
        self.visited_urls.append(new_url)

    def add_unvisited_list(self, new_url):
        new_url = self.isHave(new_url)
        if new_url is None:
            return
        self.unvisited_urls.append(new_url)

    def add_unvisited_list_with_links(self, links):
        for link in links:
            self.add_unvisited_list(link)

    def remove_visited(self, rm_url):
        self.visited_urls.remove(rm_url)
    
    def pop_unvisited(self):
        try:
            tmpUrl = self.unvisited_urls.pop()
            return tmpUrl
        except expression as identifier:
            return None

    def is_null_unvisited(self):
        return len(self.unvisited_urls) == 0
 
def get_all_href(html_data):
    re_str = "(?<=href=\").*?(?=\")|(?<=href=\').*?(?=\')"
    pages = re.findall(re_str, html_data)
    newlinks = re_link(pages)
    return newlinks

def re_link(links):
    newlinks = []
    for link in links:
        if link == '#' or link == "/" or link.find("javascript") != -1 or link.find("http") != -1:
            continue
        newlinks.append(link)
    return newlinks

def url_protocol(url):
    '''
    获取输入的url地址的协议，是http、https等
    '''
    print('该站使用的协议是：' + re.findall(r'.*(?=://)',url)[0])
    return re.findall(r'.*(?=://)',url)[0]

def domain(url):
    '''
    处理用户输入的url，并为后续判断是否为一个站点的url做准备，爬取的时候不能爬到其它站，那么爬取将无止境
    :return: sameurl
    '''
    #将完整的url中的http://删除
    up = url_protocol(url)

    url = url.replace(up + '://','')
    #判断删除http://之后的url有没有www，如果没有就加上‘www.’，但不存储，
    #只是为了同化所有将要处理的url，都有了‘www.’之后，
    #就可以找以‘www.’开始的到第一个‘/’结束中的所有字符串作为该站的主域名
    if re.findall(r'^www',url) == []:
        sameurl = 'www.' + url
        if sameurl.find('/') != -1:
            sameurl = re.findall(r'(?<=www.).*?(?=/)', sameurl)[0]
        else:
            sameurl = sameurl + '/'
            sameurl = re.findall(r'(?<=www.).*?(?=/)', sameurl)[0]
    else:
        if url.find('/') != -1:
            sameurl = re.findall(r'(?<=www.).*?(?=/)', url)[0]
        else:
            sameurl = url + '/'
            sameurl = re.findall(r'(?<=www.).*?(?=/)', sameurl)[0]
    print('同站域名地址：' + sameurl)
    return sameurl

def links_add_baseurl(links, url):
    newLinks = []
    # print links
    for link in links:

        if link[-1] == '/':   #最后一个字符不是_
            link = link[0:len(link)-1]
            # print link

        newLinks.append(baseURL + link)
    return newLinks

class Sliper: 
    def __init__(self,url):
        self.linkQuence = linkQuence()   #引入linkQuence类
        self.linkQuence.add_unvisited_list(url)   #并将需要爬取的url添加进linkQuence对列中
        self.current_deepth = 1    #设置爬取的深度
        domain_url = domain(baseURL)

        '''
        这里需要注意:
        爬取分为：***先深度后广度***和***先广度和后深度***
        1、如果是先深度后广度，那么给定一个url，然后从其页面中的任意一个可用链接进行深度爬取，很可能无限至循环下去
        （在处理不当的时候，但一般情况下大家都会处理的很好，无非是判断哪些url是已经爬取过的，哪些是新爬取到的url）
        2、如果是先广度后深度，就是将一个url页面中的所有链接进行爬取，然后分类处理过滤
        （在这种处理不当的时候也会出现无限循环的可能，但一般情况下大家都会处理的很好，无非是判断哪些url是已经爬取过的，哪些是新爬取到的url）
        '''

    def get_PageLinks(self, url):
        '''
        获取某个url的所有链接
        '''
        # print "获取当前页面的所有 Href 链接:"+ url
        req = urllib2.Request(baseURL, headers=header)
        html = urllib2.urlopen(req)
        htmldata = html.read()
        links = get_all_href(htmldata)
        links = links_add_baseurl(links, url)
        # for page in links:
        #     print page
        return links

    def caw(self, crawl_deepth = 1):
        while self.current_deepth < crawl_deepth:
            #TODO :这里会形成一个死循环～不能做到深度控制，这里需要控制下  
            pageList = self.linkQuence.get_unvisited_list()
            tempList = pageList[:]
            for page in tempList:
                self.linkQuence.add_visited_list(page)

                loading_url = page
                if loading_url is None or loading_url == '':
                    continue
                self.linkQuence.add_visited_list(loading_url)
                links = self.get_PageLinks(loading_url)
                dPrintLinks("获取到的连接为", links, "层级{}".format(crawl_deepth-1))
                self.linkQuence.add_unvisited_list_with_links(links)
                self.linkQuence.pop_unvisited()

            print 'links.len is {} by link {}'.format(len(self.linkQuence.get_unvisited_list()), page)
            self.current_deepth += 1
        return self.linkQuence.visited_urls

def dPrintLinks(beginStr, links, lastStr):
    for link in links:
        print '{} {} {}'.format(beginStr, link, lastStr)

def main():
    sliper = Sliper(baseURL)
    print sliper.caw(3)

main()