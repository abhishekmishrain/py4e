largest = None
smallest = None
while True:
    sn = input("Enter a number: ")
    if sn == "done" : break
    try:
        num = int(sn)
    except:
        print('Invalid input')
        continue
    #print(num)
    if (largest == None):
        largest = num
        smallest = num
        continue
    if (num > largest):
        largest = num
    if (num < smallest):
        smallest = num

print("Maximum is", largest)
print("Minimum is", smallest)
