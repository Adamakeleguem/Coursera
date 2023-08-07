list_email = []
counts = dict()
bigcount=-1
bigword=None
fname = input("Enter file:")
if len(fname) < 1:
    fname = "mbox-short.txt"
handle = open(fname,'r')
for line in handle:
    if not line.strip():
        continue
    if line.startswith('From '):
        words = line.split()
        if len(words) > 1 and ":" not in words[1]:
            email_address = words[1]
            list_email.append(email_address)
for word in list_email:
    counts[word]=counts.get(word,0)+1
for word,count in counts.items():
  if count> bigcount:
    bigword=word
    bigcount=count
print(bigword,bigcount)