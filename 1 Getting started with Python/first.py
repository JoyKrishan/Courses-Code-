num = int(input("Enter a number: "))
mod=''
out=''
while num>0:
    mod_num=num
    num=int(num/2)
    mod=str(mod_num%2)+mod
for i in mod:
    if i=='1':
        out=out+i
print(int(out,2))
