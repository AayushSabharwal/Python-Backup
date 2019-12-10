#maximum subarray problem    
    
n = int(input("Enter n"))
l = []
pos = 0 #count of positives
neg = 0 #count of negatives
zer = 0 #count of zeroes
for i in range(n):
    l.append(int(input("Enter element")))
    if(l[i] > 0):
        pos = pos + 1
    elif(l[i] == 0):
        zer = zer + 1
    else:
        neg = neg + 1

if(neg == 0):
    #max subarray is entire array
    ss = 0
    for i in range(n):
        ss = ss + l[i]
    print(ss)
elif(pos == 0 or pos == 1):
    #max subarray is max element
    mx = l[0]
    for i in range(n):
        if(l[i] > mx):
            mx = l[i]
    print(mx)
else:
    maxSum = l[0]
    curSum = l[0]
    for i in range(1, n):
        if(l[i] < curSum + l[i]):
            curSum = curSum + l[i]
        else:
            curSum = l[i]
        if(curSum > maxSum):
            maxSum = curSum
    print(maxSum)
    