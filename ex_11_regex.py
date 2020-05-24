import re

#fname = input("Enter file name: ")
#if len(fname) < 1 : fname = "ex_11_file2.txt"


#fh = open(fname, "r")

#print(sum([int(i) for i in re.findall(r"[0-9]+", fh.read())]))
print(sum([int(i) for i in re.findall(r"[0-9]+", open(input("Enter file name: ")).read())]))
