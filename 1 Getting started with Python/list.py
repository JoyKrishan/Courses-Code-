fname=input('Enter the file name')
lst=list()
try:
    fhandle=open(fname)
except:
    print('file not found:', fname)
    quit()
for line in fhandle:
    line=line.strip()
    words=line.split()
    for word in words:
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)
