""" ## file 
name_file=input('Enter file: ')
handle=open(name_file)
counts=dict()
for line in handle:
  words=line.split()
  for word in words:
    counts[word]=counts.get(word,0)+1
bigcount=None
bigword=None
for word,count in counts.items():
  if bigcount is None or count>bigcount:
    bigword=word
    bigcount=count
print(bigword,bigcount) """
staf=dict()
print(staf.get('adama'),-1)
