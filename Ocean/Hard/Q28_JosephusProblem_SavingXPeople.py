#Josephus, saving x people
n = int(input("Enter n"))
k = int(input("Enter k"))
x = int(input("Enter x"))

ppl = []
for i in range(1, n+1):
    ppl.append(i)

cur = k%n - 1
while(len(ppl) != x):
    ppl.pop(cur)
    cur = (cur + k - 1)%len(ppl)

print(ppl)