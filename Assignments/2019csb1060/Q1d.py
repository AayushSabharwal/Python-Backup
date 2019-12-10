#Q1d to implement mergesort

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

l = [int(x) for x in input().split(' ')]
l =mergesort(l)
for i in l:
    print(i, end = ' ')