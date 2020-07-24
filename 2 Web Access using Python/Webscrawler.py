from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl
import re

ctx=ssl.create_default_context()
ctx.check_hostname= False
ctx.verify_mode=ssl.CERT_NONE

url=input('Enter- ')
pos=int(input('Enter the position- '))
count=int(input('Enter the count- '))
for i in range(count):
    if i==0:
        print(re.findall('known_by_([\w]+)',url))
        pos=pos-1
        html=urllib.request.urlopen(url).read()
    else:
        html=urllib.request.urlopen(new_url).read()
    soup=BeautifulSoup(html, 'html.parser')
    #Retrieve all the anchor tags
    tags=soup('a')
    href=tags[pos]
    new_url=href.get('href', None)
    names=re.findall('known_by_([\w]+)', new_url)
    print(names)
