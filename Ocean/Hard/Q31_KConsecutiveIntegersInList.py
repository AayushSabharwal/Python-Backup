#k consecutive integers in list

def printN(s, e):
    nums = []
    for i in range(s, e+1):
        nums.append(i)
    print(nums)

n = int(input("Enter n"))
k = int(input("Enter k"))

l = []
for i in range(n):
    l.append(int(input("Enter element")))

mx = l[0]
for i in range(1, n):
    if(l[i] > mx):
        mx = l[i]

freq = []
for i in range(mx + 1):
      freq.append(0)


for i in range(n):
    freq[l[i]] = freq[l[i]] + 1

p1 = 0
p2 = 0
while(p2 != mx):
    if(p1 == p2):
        if(freq[p1] == 0):
            p1 = p1 + 1
            p2 = p2 + 1
        elif(freq[p1+1] > 0):
            p2 = p2 + 1
        else:
            p1 = p1 + 2
            p2 = p2 + 2
    elif(p2 - p1 == k-1):
        printN(p1, p2)
        if(freq[p2+1] == 0):
            p1 = p2 + 2
            p2 = p2 + 2
        else:
            p1 = p1 + 1
            p2 = p2 + 1
    else:
        if(freq[p2 + 1] > 0):
            p2 = p2 + 1
        else:
            p1 = p2 + 2
            p2 = p2 + 2

if(p2 - p1 == k-1):
    printN(p1, p2)