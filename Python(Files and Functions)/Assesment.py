str1 = "peter piper picked a peck of pickled peppers"
freq={}
for i in str1:
    print(i)
    if i not in freq:
        freq=freq.get(i, 0)+1
print(freq)
