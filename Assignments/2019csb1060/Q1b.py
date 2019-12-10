#Q1b to implement insertion sort
def insertionsort(l):
    n = len(l)
    for i in range(1, n):
        t = l[i]
        j = i-1
        while(j >= 0 and t < l[j]):
            l[j+1] = l[j]
            j = j-1
        l[j+1] = t
    return l

l = [int(x) for x in input().split(' ')]
insertionsort(l)
for i in l:
    print(i, end=' ')