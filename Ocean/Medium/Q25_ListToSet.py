#program to turn list into set
n = int(input("Enter n"))
l = []
for i in range(n):
    l.append(int(input("Enter element")))

setL = []
for i in range(len(l)):
    alreadyExists = False
    for j in range(i):
        if(l[i] == l[j]):
            alreadyExists = True
            break
    if(not alreadyExists):
        setL.append(l[i])
print(setL)