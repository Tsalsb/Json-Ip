import urllib
import json
#pulls json data from a URL
url = "http://jsonip.com"
response = urllib.urlopen(url)
data = json.loads(response.read())
print "Hello There!, Your IP Address Appears to be \n" + data['ip']
