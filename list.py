list_email = []
count = 0
fname = input("Enter file name: ")

file=open(fname, 'r')


for line in file:
    if not line.strip():
        continue
    if line.startswith('From '):
        words = line.split()
        if len(words) > 1 and ":" not in words[1]:
            email_address = words[1]
            list_email.append(email_address)
            count += 1
for address in list_email:
    print(address)
print("There were", count, "lines in the file with From as the first word")