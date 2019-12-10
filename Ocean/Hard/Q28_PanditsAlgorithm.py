def perm(n):
      a = []
      for i in range(1, n+1):
            a.append(i)
      ans = []
      k = n-2
      while(k != -1):
            ans.append(a.copy())
            l = k+1
            for i in range(l, n):
                  if(a[k] < a[i]):
                        l = i
            a[k], a[l] = a[l], a[k]
            for i in range(k+1, int((n+k)/2) + 1):
                  a[i], a[n + k - i] = a[n + k - i], a[i]
            k = -1
            for i in range(n-1):
                  if(a[i] < a[i+1] and i > k):
                        k = i

      ans.append(a)
      return ans

n = int(input())
ans = perm(n)
print(ans, len(ans))