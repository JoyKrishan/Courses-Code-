import urllib.request, urllib.parse, urllib.error
import ssl
import xml.etree.ElementTree as ET

ctx=ssl.create_default_context()
ctx.check_hostname= False
ctx.verify_mode=ssl.CERT_NONE

url=input('Enter- ')
xml=urllib.request.urlopen(url, context=ctx).read()

tree=ET.fromstring(xml)
comment_tags=tree.findall('comments/comment')
print("Count:", len(comment_tags))

lst=list()
for tag in comment_tags:
    value=tag.find('count').text
    lst.append(int(value))
print(lst)
print(sum(lst))
