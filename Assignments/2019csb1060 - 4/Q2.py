#Q2 find sorted position of given element in unsorted list
n = int(input())
l = [int(x) for x in input().split(" ")]
k = int(input())
num = l[k-1]
less = []
more = []
for i in range(n):
    if(i != k-1):
        if(l[i] < num):
            less.append(l[i])
        else:
            more.append(l[i])

print(len(less) + 1)