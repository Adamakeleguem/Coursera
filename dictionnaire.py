purse=dict()
purse['money']=12
purse['candy']=3
purse['tissues']=75
print(purse)
print(purse['candy'])
purse['candy']=purse['tissues']*10
print(purse)
# Comparaison entre list et dictionary
ddd=dict()
dele=list()

ddd['adaa']=254
ddd['alaa']=252
dele.append(254)
dele.append(253)
print(ddd)
print(dele)


counts=dict()
names=['csev','cwen','csev','zqian','cwen']
for name in names:
    if name not in counts:
        counts[name]=1
    else:
        counts[name]=counts[name]+1
print(counts)

if name in counts:
    x=counts[name]
else:
    x=0
x=counts.get(name,0)
# using get

counts=dict()
names=['csev','cwen','csev','zqian','cwen']
for name in names:
    # this line combine if and else
    counts[name]=counts.get(name,0)+1
print(counts)

# dictionnarie 9.3 
counts=dict()
print('Entrer les lignes de textes')
#fname = input("Enter file name: ")
#fh = open(fname)
""" line=input('')
words=line.split()
print('words:',words)
for word in words:
    counts[word]=counts.get(word,0)+1
print('Counts: ', counts) """
# un programme qui parcours un dictionnaire

counts={'chien':1, 'chat': 4, 'cheval':256, 'elephant':1254}
for key in counts:
    print(key, counts[key])
