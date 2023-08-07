c={'a':10,'b':1,'c':22}
print(sorted([(v,k)for k,v in c.items()]))
# list comprehension creates a dynamic list. In this cas , we make a list of reversed tuples and then sort it.
#[(v,k)for k,v in c.items()]=>equivalent 
lst=list()
counts=dict()
for key,val in counts.items():
    newtup=(val,key)
    lst.append(newtup)