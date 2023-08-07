fhand=open('mbox-short.txt')
di=dict()
list_date=[]
list_mouth = []
for line in fhand:
    if not line.strip():
        continue
    if line.startswith('From '):
        words = line.split()
        if len(words) > 1 and ":" not in words[1]:
            mount = words[5]
            list_date.append(mount)
for w in list_date:
    list_mouth.append(w[:2])

for w in list_mouth:
    di[w]=di.get(w,0)+1

x=sorted(di.items())
for k,v in x:
    print(k,v)