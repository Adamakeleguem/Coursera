""" d={'a':10,'b':'1','c':22}
t=sorted(d.items())
print(t)
for k,v in sorted(d.items()):
    print(k,v) """
# short by values instead of key
""" c={'a':10,'b':1,'c':22}
tmp=list()
for k,v in c.items():
    tmp.append((v,k))
print(tmp) """

fhand=open('mbox-short.txt')
""" counts=dict() """
di=dict()
list_mouth = []
for line in fhand:
    if not line.strip():
        continue
    if line.startswith('From '):
        words = line.split()
        if len(words) > 1 and ":" not in words[1]:
            mount = words[2]
            list_mouth.append(mount)
for w in list_mouth:
    di[w]=di.get(w,0)+1



""" for line in fhand:
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1
print(counts) """



""" lst=list()
for key,val in counts.items():
    newtup=(val,key)
    lst.append(newtup)

lst=sorted(lst,reverse=True)
print(lst)
for val,key in lst[:10]:
    print(key,val) """