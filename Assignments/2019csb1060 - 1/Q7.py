#program to find all numbers divisible by 7 but not 5 between 2000 and 3200 (both included)
l = []
for i in range(2000, 3201):
    if(i%7 == 0) and (i%5 != 0):
        l.append(i)
print('numbers between 2000 and 3200 divisible by 7 but not 5 are ', l)
