list_email = []
count = 0
fname = input("Enter file:")
if len(fname) < 1:
    fname = "mbox-short.txt"
handle = open(fname,'r')
for line in handle:
    if not line.strip():
        continue
    if line.startswith('From'):
        