import json
data='''
{
    "name": "Joy Krishan",
    "phone":{
        "type":"intl",
        "number":"+8801746120146"
    },
    "email":{
    "hide":"yes"
    }
}'''

info=json.loads(data)
print(type(info))
print(info["name"])
print(info["phone"]["number"])

data_2='''
[
    { "name":"Joy Krishan",
      "ID":"007",
      "On the way to":"10000 hours rule"
    },
    { "name":"Dr Chuck",
      "ID":"009",
      "On the way to":"Best Teacher Ever"

    }
]'''

info=json.loads(data_2)
print(type(info))
for item in info:
    print(item["name"], ":", item["On the way to"])
