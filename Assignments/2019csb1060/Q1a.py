#Q1a to implement bubble sort

def bubblesort(l):
    n = len(l)
    for i in range(n-1):
        for j in range(n-1-i):
            if(l[j] > l[j+1]):
                l[j], l[j+1] = l[j+1], l[j]
    return l

l = [int(x) for x in input().split(' ')]
bubblesort(l)
for i in l:
    print(i, end=' ')