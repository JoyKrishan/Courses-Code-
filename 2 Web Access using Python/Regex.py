import re
fname=input('Enter the file name\n')
lst=list()
try:
    fhandle=open(fname)
except:
    print('File could not be found',fname)
    quit()
for line in fhandle:
    if re.search('[0-9]+',line):
        num=re.findall('[0-9]+',line)
        for i in num:
            lst.append(int(i))
print(sum(lst))
