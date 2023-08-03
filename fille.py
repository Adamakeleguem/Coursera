import os
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    list=line.split()
    for word in list:
        if word not in [c.lower() for c in lst]:
            lst.append(word)
lst.sort()
for word in lst:
    print(word)



