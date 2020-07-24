from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import re

url=input('Give the Url')
fhandle=urllib.request.urlopen(url)
data=fhandle.read()
soup=BeautifulSoup(data, 'html.parser')
tags=soup('tr')
lst=list()
for tag in tags:
    print(tags)
