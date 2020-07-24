largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    try:
        num=int(num)
    except:
        if num == 'done':
            break
        else:
            print('Invalid Input')
            continue
    if smallest is None and largest is None:
        smallest=num
        largest=num
    else:
            if(num<smallest):
                smallest=num
            elif(num>largest):
                largest=num
print("Maximum", largest)
print("Minimum", smallest)
