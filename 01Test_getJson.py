import urllib2, json
from geoip import geolite2

# url = "https://fcc-weather-api.glitch.me/api/current?lat=35&lon=139"

# http://ipinfo.io/json?callback=JSON_CALLBACK
def getJson(url):
    header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
            , "Connection": "keep-alive"
         }
    print "url ===" + url
    req = urllib2.Request(url, headers=header)
    res = urllib2.urlopen(req)
    
    res_data = res.read()
    print "res_data" + res_data[57:]
    print res_data
    json_data = json.loads(res_data)
    print json_data
    return json_data


base_url = "https://fcc-weather-api.glitch.me/api/current?"
where_url = "http://ipinfo.io/json?callback=JSON_CALLBACK"

where = getJson(where_url)
print where("loc")


