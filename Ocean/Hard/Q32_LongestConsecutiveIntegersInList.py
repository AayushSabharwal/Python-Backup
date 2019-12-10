#longest consecutive integers in list

def retList(s, e):
    nums = []
    for i in range(s, e+1):
        nums.append(i)
    return nums

n = int(input("Enter n"))

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
longestSeq = []
while(p2 != mx):
    if(p1 == p2):
        if(freq[p1] == 0):
            p1 = p1 + 1
            p2 = p2 + 1
        elif(freq[p1+1] > 0):
            p2 = p2 + 1
            cseq = retList(p1, p2)
            if(len(cseq) > len(longestSeq)):
                longestSeq = cseq
        else:
            p1 = p1 + 2
            p2 = p2 + 2
    elif(freq[p2+1] > 0):
        p2 = p2 + 1
        cseq = retList(p1, p2)
        if(len(cseq) > len(longestSeq)):
            longestSeq = cseq
    else:
        p2 = p2 + 2
        p1 = p2

print(longestSeq)