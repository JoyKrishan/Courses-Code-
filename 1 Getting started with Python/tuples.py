fname=input('Enter the file name\n')
count=dict()
try:
    fhandle=open(fname)
except:
    print('File could not be found', fname)
for line in fhandle:
    if not line.startswith('From') or line.startswith('From:'):
        continue
    line=line.rstrip()
    words=line.split()
    for word in words:
        if ":" in word:
            first=word.split(":")
            hour=first[0]
            count[hour]=count.get(hour,0)+1
lst=list()
for key,value in count.items():
    lst.append((key, value))
lst=sorted(lst)
for a,b in lst:
    print(a,b)
