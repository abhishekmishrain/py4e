# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
num = 0
#sum = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    #print(line.rstrip())
    dotpos = line.find('.')
    num = num + float(line[dotpos-1:])
    #sum = sum + num;
    count = count + 1
    #print(num)

#print("Sum: ", sum)
#print("Count:", count)
print("Average spam confidence:", num / count)

#print("Done")
