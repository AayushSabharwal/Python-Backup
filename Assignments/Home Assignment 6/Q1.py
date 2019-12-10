import random

def myshuffle(l):
      size = len(l)
      indexes = []
      for i in range(size):
            indexes.append(i)
      
      order = []
      for i in range(size):
            ind = random.randint(0, len(indexes)-1)
            order.append(indexes[ind])
            indexes.remove(indexes[ind])
      
      shuffled = []
      for i in range(size):
            shuffled.append(l[order[i]])
      
      return shuffled