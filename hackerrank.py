for i in range(10):
      n = input()
      if(n == ''):
            break
      n = int(n)
      l = [n]
      updated = True
      while updated:
            updated = False
            tmp = []
            for i in l:
                  split = i//2 + i//3 + i//4
                  if(split > i):
                        tmp.extend([i//2, i//3, i//4])
                        updated = True
                  else:
                        tmp.append(i)
            l = tmp[:]
      print(sum(l))