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

def mergesort(l):
    if(len(l) == 0 or len(l) == 1):
        return l

    left = mergesort(l[:int(len(l)/2)])
    right = mergesort(l[int(len(l)/2):])
    
    n = len(left)
    m = len(right)
    i = 0
    j = 0
    ans = []
    while(i < n and j < m):
        if(left[i] == right[j]):
            ans.append(left[i])
            ans.append(right[j])
            i = i+1
            j = j+1
        elif(left[i] < right[j]):
            ans.append(left[i])
            i = i+1
        else:
            ans.append(right[j])
            j = j+1
    
    while(i < n):
        ans.append(left[i])
        i = i+1
    while(j < m):
        ans.append(right[j])
        j = j+1
    
    return ans

def bubblesort(l):
    n = len(l)
    for i in range(n-1):
        for j in range(n-1-i):
            if(l[j] > l[j+1]):
                l[j], l[j+1] = l[j+1], l[j]
    return l

def comparativegraph():
    import random
    import time
    from matplotlib import pyplot as plt
    
    #bubtime = []
    mergetime = []
    quicktime = []
    for i in range(1, 5000):
        l = random.sample(range(100000), i)
        
        #start = time.time()
        #bubblesort(l.copy())
        #end = time.time()
        #bubtime.append(end-start)
        
        start = time.time()
        mergesort(l.copy())
        end = time.time()
        mergetime.append(end-start)
        
        start = time.time()
        quicksort(l.copy())
        end = time.time()
        quicktime.append(end-start)
    
    x = [i for i in range(1, 5000)]
    #plt.plot(x, bubtime)
    plt.plot(x, mergetime)
    plt.plot(x, quicktime)
    plt.legend(['merge', 'quick'])