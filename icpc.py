t = int(input())
for i in range(t):
      n, k = [int(x) for x in input().split()]
      s = input()
      p = []
      for i in range(k):
            p.append(input())
      
      ans = []
      valid = list(range(len(p)))
      i = 0
      prev = valid.copy()
      while(i < n):
            for pen in valid:
                  if(s[i] not in p[pen]):
                        valid.remove(pen)
            if(len(valid) == 0):
                  ans.append(prev[0])
                  valid = p.copy()
                  prev = p.copy()
            else:
                  prev = valid.copy()
            i = i + 1
      
      for i in ans:
            print(i, end = ' ')
            
      print()