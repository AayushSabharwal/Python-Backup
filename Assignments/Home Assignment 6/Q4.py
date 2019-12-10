import random
def biasedcoin():
      ans = random.randint(0, 3)
      if(ans == 0):
            return 'H'
      else:
            return 'T'