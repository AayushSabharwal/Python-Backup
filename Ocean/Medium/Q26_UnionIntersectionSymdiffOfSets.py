#union intersection and symDiff of 2 sets
n1 = int(input("Size of first set"))
l1 = []
for i in range(n1):
    l1.append(int(input("Enter element")))

n2 = int(input("Size of second set"))
l2 = []
for i in range(n2):
    l2.append(int(input("Enter element")))

if(n1 > n2):
    n1, n2 = n2, n1
    l1, l2 = l2, l1

union = l2
intersection = []
symDiff = []
for i in range(n1):
    alreadyExists = False
    for j in range(len(union)):
        if(union[j] == l1[i]):
            alreadyExists = True
            break
    if(not alreadyExists):
        union.append(l1[i])

for i in range(n1):
    common = False
    for j in range(n2):
        if(l2[j] == l1[i]):
            common = True
            break
    if(common):
        intersection.append(l1[i])
    else:
        symDiff.append(l1[i])

intLen = len(intersection)
for i in range(n2):
    common = False
    for j in range(intLen):
        if(intersection[j] == l2[i]):
            common = True
            break
    if(not common):
        symDiff.append(l2[i])

print('union = ', union)
print('intersection = ', intersection)
print('symdiff = ', symDiff)