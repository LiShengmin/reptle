import urllib
url ="http://qiniuuwmp3.changba.com/715249748.mp3"
name = "夏日广场.mp3"
print 'loading'
urllib.urlretrieve(url, name) 
print 'finish'