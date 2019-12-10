#Q1e to implement quicksort

def quicksort(l):
    if(len(l) <= 1):
        return l
    less = []
    more = []
    n = len(l)
    pivot = 0
    for i in range(1, n):
        if(l[i] < l[pivot]):
            less.append(l[i])
        else:
            more.append(l[i])
    
    less = quicksort(less)
    more = quicksort(more)
    less.append(l[pivot])
    less.extend(more)
    return less

l = [int(x) for x in input().split(' ')]
l = quicksort(l)
for i in l:
    print(i, end=' ')