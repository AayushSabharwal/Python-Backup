#program to solve Josephus problem

n = int(input("Enter n"))   #no of people in circle
k = int(input("Enter k"))   #k-1 people are skipped, kth is killed

ppl = []
for i in range(1,n+1):
    ppl.append(i)

cur = k%n-1
while(len(ppl) > 1):
    ppl.pop(cur)
    cur = cur + k - 1
    cur = cur%len(ppl)

print(ppl)