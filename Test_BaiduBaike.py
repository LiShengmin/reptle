import requests, re

url = 'https://wenku.baidu.com/view/f4ef56233169a4517723a3bc.html'

res = requests.get(url).text
print res