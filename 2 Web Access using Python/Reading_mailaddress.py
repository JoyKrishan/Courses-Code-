fname=input("Enter the Filename")
count=0
try:
    fhandle=open(fname, 'r')
except:
    print('File not found:', fname)
    quit()
for line in fhandle:
    if not line.startswith('From'):
        continue
    if not line.startswith('From:'):
        words=line.split()
        print(words[1])
        count=count+1
print(count)
