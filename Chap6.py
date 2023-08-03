""" fruit='banana'
word=input("Enter word ")
word=word.lower()
if word=='banana':
    print('All right, bananas.')
elif word< 'banana':
    print('Your word, '+word+', comes before banana.')
elif word >'banana':
    print('Your word, '+word+', comes after banana.')
else:
    print('All right, bananas.')
#lists the method of string classd
dir(word)
#print the type of word 
type(word)

 text = "X-DSPAM-Confidence:    0.8475"
zer=text.find('0')
print(text[zer:])

fhand=open('mbow-short.txt')
for line in fhand:
    line=line.rstrip()
    if not '@uct.ac.za' in line:
        continue
    print(line) 
# Use words.txt as the file name
 import os
 fname = input("Enter file name: ")
fh = open(fname)
contenu=fh.read()
textupp=contenu.upper().strip()
print(textupp)
# Use the file name mbox-short.txt as the file name
# Use the file name mbox-short.txt as the file name
 fname = input("Enter file name: ")
fh = open(fname)
count=0
val=0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    
    val=val+float(line.split(':')[1].strip())
    count=count+1
print("Average spam confidence:", val/count)

friends=['Ousmane','Salifou', 'omo', 'Issaka']
for friend in friends:
    print("Tu es le meilleur",friend)
les list sont mutables mais les string non
manipulation deslistes 

a=[1,2,3]
b=[4,5,6]
c=a+b
d=b+a
print(c)
print(d)
dir(a) """
""" abc='we are Africa'
lsite=abc.split()
print(lsite) """
""" fruit='Banana'
fruit[0]='b'
print(fruit) """
""" (x,y)=(2,'Adama')
print(x)
print(y) """

""" d=dict()
d['csev']=2
d['cwen']=4

for (k,v) in d.items():
    print(k,v)
tups=d.items()
print(tups)
tu=tuple()
print(dir(tu)) """

d={'a':10,'b':5, 'c':5}
t=sorted(d.items())
print(t)
for r,v in t:
    print(r,v)
# how to short by key
# if we could construct a list of tuples of the form
# (value, key) we could sort by value
# we do this with a for loop that creates a list of tuples
""" c={'a':10, 'b':1, 'c':22}
temp=list()
for k,v in c.items():
    temp.append((k,v))
print(temp)
temp=sorted(temp,reverse=True)
print(temp) """

hand="Print file name: "
fhand=open(hand)
counts=dict()
for ligne in fhand:
    words=ligne.split()
    for word in words:
        counts[word]=counts.get(word,0)+1

# using list 

lst=list()
for val,key in counts.items():
    new_t=(val,key)
    lst.append(new_t)

lst=sorted(lst,reverse=True)
for val,key in lst[:lst]:
    print(val,key)