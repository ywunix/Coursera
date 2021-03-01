# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

'''
url = input('Enter - ')
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_42.html"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
tags = soup('span')
_sum = 0
for tag in tags:
    # Look at the parts of a tag
    try:
        val = int(tag.contents[0])
    except:
        print("Not Integer, Skip")
        continue
    _sum += val

print(_sum)
'''

def getNextUrl(url, pos):
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    tags = soup('a')
    tag = tags[pos]
    return tag.get('href', None)



url = input('Enter URL: ')
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
count = input('Enter count: ')
if len(count) < 1:
    count = 4
else:
    count = int(count)
pos = input('Enter position: ')
if len(pos) < 1:
    pos = 3
else:
    pos = int(pos)


for _ in range(count):
    print(url)
    url =  getNextUrl(url, pos - 1)
    if url is None:
        break
print(url)