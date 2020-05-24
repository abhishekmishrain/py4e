fname = input("Enter file name: ")
if len(fname) < 1 : fname = "data.txt"

fh = open(fname)
count = 0

d = dict()

for line in fh:
    #line.rstrip()
    if line.startswith('From') and line[4] != ':':
            words = line.split()
            #print(words[1])
            d[words[1]] = d.get(words[1],0) + 1

#print(d)

maxcount = None
maxname = None
for name, count in d.items():
    if (maxcount == None or maxcount < count):
        maxcount = count
        maxname = name

print(maxname, maxcount)
