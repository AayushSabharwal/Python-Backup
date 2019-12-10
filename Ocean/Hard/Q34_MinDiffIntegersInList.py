#closest pair of integers

n = int(input("Enter n"))
l = []
l.append(int(input("Enter element")))
mx = l[0]
for i in range(1, n):
    l.append(int(input("Enter element")))
    if(l[i] > mx):
        mx = l[i]

freq = [0]*(mx + 1)
for i in range(n):
    freq[l[i]] = freq[l[i]] + 1

l.clear()
for i in range(mx+1):
    while(freq[i] > 0):
        l.append(i)
        freq[i] = freq[i] - 1

print(l)

minDiff = l[1]-l[0]
for i in range(1, n-1):
    t = l[i+1] - l[i]
    minDiff = t if t < minDiff else minDiff

print(minDiff)