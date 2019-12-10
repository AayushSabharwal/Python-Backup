#consecutive integers in list
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

for i in range(mx):
    if(freq[i] > 0 and freq[i+1] > 0):
        print(i, ' ', i+1)