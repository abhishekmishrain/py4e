def computepay(hours, rate):
    #print('Hours', hours, 'Rate', rate)
    pay = hours * rate
    if (hours > 40): pay = pay + (hours - 40) * rate * 0.5
    #print('Returning pay:', pay)
    return pay

h = float(input ('Hours:'))
r = float(input ('Rate:'))
p = computepay(h, r)
print ('Pay', p)
