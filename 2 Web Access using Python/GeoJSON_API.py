import urllib.request, urllib.parse, urllib.error
import json

api_key=42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

while True:
    address=input('Enter address')
    if len(address)<1:break

    url=serviceurl+urllib.parse.urlencode({'address':address, 'key':api_key})
    print('Retrieving URL', url)
    uh=urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    try:
        js=json.loads(data)
    except:
        js=None
    if not js or 'status' not in js or js["status"] != "OK":
        print("Failed --- To --- Retrieve")
        #print(data)
        continue
    print(json.dumps(js, indent=4))
    lng=js["results"][0]["geometry"]["location"]["lng"]
    lat=js["results"][0]["geometry"]["location"]["lat"]
    print("lat", lat, "lng", lng)
    location=js["results"][0]["formatted_address"]
    print("Address:", location)
    placeID=js["results"][0]["place_id"]
    print("Place ID:", placeID)
