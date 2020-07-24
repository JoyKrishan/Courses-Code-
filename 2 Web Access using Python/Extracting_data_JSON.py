import urllib.request, urllib.parse, urllib.error
import ssl
import json

#Retrieving data using https
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url=input('Enter url-')
uh=urllib.request.urlopen(url, context=ctx)
data=uh.read().decode()
js=json.loads(data)
print(json.dumps(js, indent=4))
value=list()
for i in js["comments"]:
    value.append(i["count"])
print(sum(value))
