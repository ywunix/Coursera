import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_42.json"
connection = urllib.request.urlopen(url, context=ctx)

js = json.loads(connection.read().decode())
lst = js["comments"]
_sum = 0
for item in lst:
    _sum += item['count']
print(_sum)