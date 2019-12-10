#Q1c to implement selection sort

def selectionsort(l):
    n = len(l)
    for i in range(n-1):
        mn = i
        for j in range(i+1, n):
            if(l[j] < l[mn]):
                mn = j
        l[i], l[mn] = l[mn], l[i]
    return l

l = [int(x) for x in input().split(' ')]
selectionsort(l)
for i in l:
    print(i, end=' ')