#To find the kth smallest number in a list
def kth(l,k):
	for i in range(k-1):
		mn = l[0]
		for j in l:
			if (j<mn):
				mn = j
		l.remove(mn)
	mn = l[0]
	for i in l:
		if (mn > i):
			mn = i
	return mn


def kth_ing(l, k):
    pivot = l[0]
    less = []
    more = []
    for i in range(1,len(l)):
        if(l[i] < pivot):
            less.append(l[i])
        else:
            more.append(l[i])
    
    if(len(less) == k-1):
        return pivot
    elif(len(less) > k-1):
        return kth_ing(less, k)
    else:
        return kth_ing(more, k - len(less) - 1)