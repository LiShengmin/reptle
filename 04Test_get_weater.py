import urllib, json
import Test_get_ip

ip = Test_get_ip.get_local_ip()
print 'adress_ip='+ ip
location = Test_get_ip.get_location(ip)
loc = location[0]

baseURL = 'https://fcc-weather-api.glitch.me/api/current?'
url = '{baseURL}lat={lat}&lon={loc}'.format(baseURL=baseURL, lat= location[0], loc=location[1])
# url = "https://fcc-weather-api.glitch.me/api/current?lat=40.6522&lon=109.8222"
print url
response = urllib.urlopen(url)
data = json.loads(response.read())
print 'address' + data[u'name']
print data[u'coord']
print 'image' + data[u'weather'][0][u'icon']
print '温度_摄氏度:{tmp}'.format(tmp=data[u'main'][u'temp'])
print '温度_华氏度:{tmp}'.format(tmp=data[u'main'][u'temp'] * 1.8 + 32) 
