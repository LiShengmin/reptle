#!/bin/bash
# -*-coding:utf-8-*-


import urllib2


def findUrls(baseURL):
    return ''

def is_can_conntent(url): 
    '''
    使用requests.get方法判断url是否正确,并返回url
    :return:
    '''
    try:
        requests.get(url)
        return url
    except:
        print('please input the correct url!!!')
        #exit(-1)   #如果url是固定写入的，那么必须添加此句，否则会一直循环
    return url_is_correct()


def same_url(url):
    '''
    处理用户输入的url，并为后续判断是否为一个站点的url做准备，爬取的时候不能爬到其它站，那么爬取将无止境
    :return: sameurl
    '''
    #将完整的url中的http://删除
    url = url.replace(urlprotocol + '://','')
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

class linkQuence:
'''
处理url的类，对已访问过的和未访问过的进行记录，待后续使用
:visited_urls       :
:unvisited_urls     :
'''
    def __init__(self):
        self.visited_urls = [] 
        self.unvisited_urls = []

    def get_visited_list(self):
        return self.visited_urls

    def get_unvisited_list(self):
        return self.unvisited_urls
    
    def add_visited_list(self, new_url):
        self.visited_urls.append(new_url)

    def add_unvisited_list(self, new_url):
        self.unvisited_urls.append(new_url)

    def remove_visited(self, rm_url):
        self.visited_urls.remove(rm_url)
    
    def pop_unvisited:(self):
        try:
            return self.unvisited_urls.pop()
        except expression as identifier:
            return None

    def is_null_unvisited(self):
        return len(self.unvisited_urls) == 0

