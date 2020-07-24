from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl
import re

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url=input('Enter- ')
html=urllib.request.urlopen(url, context=ctx).read()
soup=BeautifulSoup(html, 'html.parser')

#Retrieve all the span tags
tags=soup('span')
values=list()
for tag in tags:
    tag=str(tag)
    vlist=re.findall('[0-9]+', tag)
    for i in vlist:
        values.append(int(i))
print(sum(values))
