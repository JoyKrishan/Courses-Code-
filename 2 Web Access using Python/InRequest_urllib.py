import urllib.request, urllib.parse, urllib.error

count=dict()
fhandle=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhandle:
    words=line.decode().strip().split()
    for word in words:
        count[word]=count.get(word,0)+1
lst=list()
for key,value in count.items():
    lst.append((value,key))
lst=sorted(lst)
for key,value in lst:
    print(value, ":" ,key)
