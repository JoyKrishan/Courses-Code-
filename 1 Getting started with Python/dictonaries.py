fname=input('Enter the file name\n')
count=dict()
try:
    fhandle=open(fname)
except:
    print('Hey no such file do not exist:',fname)
    quit()
for line in fhandle:
    if not line.startswith('From') or line.startswith('From:'):
        continue
    line=line.rstrip()
    words=line.split()
    for word in words:
        if '@' in word:
            count[word]=count.get(word,0)+1
Max_email=None
Max_count=None
for word,count in count.items():
    if Max_count is None or Max_count<count:
        Max_email=word
        Max_count=count
print(Max_email,Max_count)
