fname=input('Give the file name')
count=0
sum=0
try:
    fhandle=open(fname, 'r')
except:
    print('File not found', fname)
    quit()
for line in fhandle:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    pos=line.find(':')
    line=line[pos+1:]
    line=line.strip()
    fl=float(line)
    sum=sum+fl
    count+=1
print('Average spam Confidence:', sum/count)
