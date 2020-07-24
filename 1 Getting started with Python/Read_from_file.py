fname=input('Name of the file to read')
try:
    fhandle=open(fname)
except:
    print('File not found',fname)
    quit()
for line in fhandle:
    line=line.rstrip()
    print(line.upper())
