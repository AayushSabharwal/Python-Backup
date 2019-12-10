def perm(n):
      l = []
      dirn = []
      for i in range(1, n+1):
            l.append(i)
            dirn.append(-1)
      ans = []
      largestMobileInd = n-1
      while(largestMobileInd != -1):
            ans.append(l.copy())
            shift = dirn[largestMobileInd]
            l[largestMobileInd], l[largestMobileInd + shift] = l[largestMobileInd + shift], l[largestMobileInd]
            dirn[largestMobileInd], dirn[largestMobileInd + shift] = dirn[largestMobileInd + shift], dirn[largestMobileInd]
            largestMobileInd = largestMobileInd + shift
            
            for i in range(n):
                  if(l[i] > l[largestMobileInd]):
                        dirn[i] = dirn[i] * -1
            largestMobileInd = -1
            for i in range(n):
                  if(0 <= i + dirn[i] < n and l[i] > l[i + dirn[i]]):
                        if(largestMobileInd == -1):
                              largestMobileInd = i
                        elif(l[largestMobileInd] < l[i]):
                              largestMobileInd = i
      ans.append(l)
      return ans

n = int(input())
ans = perm(n)
print(ans, len(ans))