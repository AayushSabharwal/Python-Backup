#takes input as space separated list, gives output as 2 space separated integers: the two closest elements of the list
def msort(l):
      if(len(l) <= 1):
            return l;
      
      l1 = msort(l[0:int(len(l)/2)])
      l2 = msort(l[int(len(l)/2):len(l)])
      
      i = 0
      j = 0
      k = 0
      while(i < len(l1) and j < len(l2)):
            if(l1[i] == l2[j]):
                  l[k] = l1[i]
                  i = i + 1
                  k = k + 1
                  l[k] = l2[j]
                  j = j + 1
                  k = k + 1
            elif(l1[i] < l2[j]):
                  l[k] = l1[i]
                  i = i + 1
                  k = k + 1
            else:
                  l[k] = l2[j]
                  j = j + 1
                  k = k + 1
      while(i < len(l1)):
            l[k] = l1[i]
            i = i + 1
            k = k + 1
      
      while(j < len(l2)):
            l[k] = l2[j]
            j = j + 1
            k = k + 1
      
      return l

l = [int(x) for x in input().split()]
n = len(l)
l = msort(l)
diffs = []
for i in range(n-1):
      diffs.append(l[i+1] - l[i])

minind = 0
for i in range(len(diffs)):
      if(diffs[i] < diffs[minind]):
            minind = i

print(l[minind], l[minind + 1])
