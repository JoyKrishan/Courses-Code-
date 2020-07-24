import urllib.request, urllib.parse, urllib.error
import twurl
import ssl
import json

Twitter_url='https://apis.twitter.com/1.1/friends/list.json'

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

while True:
    accnt=input('Enter the account name-\n')
    if len(accnt)<1:
        break
    url=twurl.augment(Twitter_url,{'screen_name':accnt, 'count':'5'})
    print('Retrieved URL', url)
    connection=urllib.request.urlopen(url, context=ctx)
    data=connection.read().decode()
    print(data)
    headers=dict(connection.getheaders())
    print('Remaining limit', headers['x-rate-limit-remaining'])
    js=json.loads(data)
    print(json.dumps(js, indent=4))
