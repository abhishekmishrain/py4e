fname = input("Enter file name: ")
if len(fname) < 1 : fname = "data.txt"

fh = open(fname)
count = 0

for line in fh:
    #line.rstrip()
    if line.startswith('From') and line[4] != ':':
            words = line.split()
            print(words[1])
            count = count + 1


print("There were", count, "lines in the file with From as the first word")
