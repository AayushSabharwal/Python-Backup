#to find median of list of integers in deterministic linear time

#function to find median of list l by sorting. Used for small lists only
def simple_median(l):
      l.sort()
      #if list has odd number of elements
      #if(len(l)%2 == 1):
      return l[int(len(l)/2)] #median is middle element
      #else:
       #     return 0.5 * (l[int(len(l)/2) - 1] + l[int(len(l)/2)])      #median is average of central 2 elements

#function to find the ideal pivot through median of medians method
def find_pivot(l):
      #base case for our recursive function. If we have fewer than 5 elements, sorting and hence finding the median is trivial
      if(len(l) < 5):
            return simple_median(l)
      
      #first we divide l into chunks of atmost 5 elements
      chunks = [l[x:x+5] for x in range(0, len(l), 5)]
      
      #we consider only chunks with exactly 5 elements. It is intuitive that the only chunk that might have <5 elements is the last one
      if(len(chunks[-1]) < 5):
            chunks.pop(-1)
      
      #we now sort each chunk
      sorted_chunks = [sorted(chunk) for chunk in chunks]
      
      #we create a list of medians of the chunks. Since they are sorted, median is at index 2
      medians = [chunk[2] for chunk in sorted_chunks]
      
      #this list is now recursively passed into find_pivot, and hence we find median of medians
      return find_pivot(medians)

def find_kth_element(l, k):
      if(len(l) == 1):
            return l[0]
      pivot = find_pivot(l)
      low = []
      high = []
      pivots = []
      
      for i in l:
            if(i == pivot):
                  pivots.append(i)
            elif(i < pivot):
                  low.append(i)
            else:
                  high.append(i)

      if(k < len(low)):
            return find_kth_element(low, k)
      elif(k < len(low)+len(pivots)):
            return pivot
      else:
            return find_kth_element(high, k - len(low) - len(pivots))

def test_time(mx):
      import time
      import random
      times=[]
      for i in range(5, mx+1):
            l = random.sample(range(1000000), i)
            start = time.time()
            quickselect_median(l, pick_pivot)
            end = time.time()
            times.append(end-start)
      
      x = list(range(5, mx+1))
      from matplotlib import pyplot as plt
      plt.plot(x, times)

def test_med(mx):
      import random
      import statistics as s
      for i in range(1, mx+1):
            l = random.sample(range(10000000), i)
            a = find_kth_element(l, int(len(l)/2))
            if(i%2 == 0):
                  a = a + find_kth_element(l, int(len(l)/2)-1)
                  a = a/2
            b = s.median(l)
            if(a!=b):
                  print("A", i)
                  break
            
def nlogn_median(l):
    l = sorted(l)
    if len(l) % 2 == 1:
        return l[int(len(l) / 2)]
    else:
        return 0.5 * (l[int(len(l) / 2) - 1] + l[int(len(l) / 2)])

import random
def quickselect_median(l, pivot_fn=random.choice):
    if len(l) % 2 == 1:
        return quickselect(l, int(len(l) / 2), pivot_fn)
    else:
        return 0.5 * (quickselect(l, int(len(l) / 2) - 1, pivot_fn) +
                      quickselect(l, int(len(l) / 2), pivot_fn))


def quickselect(l, k, pivot_fn):
    """
    Select the kth element in l (0 based)
    :param l: List of numerics
    :param k: Index
    :param pivot_fn: Function to choose a pivot, defaults to random.choice
    :return: The kth element of l
    """
    if len(l) == 1:
        return l[0]

    pivot = pivot_fn(l)

    lows = [el for el in l if el < pivot]
    highs = [el for el in l if el > pivot]
    pivots = [el for el in l if el == pivot]

    if k < len(lows):
        return quickselect(lows, k, pivot_fn)
    elif k < len(lows) + len(pivots):
        # We got lucky and guessed the median
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots), pivot_fn)

def pick_pivot(l):
    """
    Pick a good pivot within l, a list of numbers
    This algorithm runs in O(n) time.
    """
    assert len(l) > 0

    # If there are < 5 items, just return the median
    if len(l) < 5:
        # In this case, we fall back on the first median function we wrote.
        # Since we only run this on a list of 5 or fewer items, it doesn't
        # depend on the length of the input and can be considered constant
        # time.
        return nlogn_median(l)

    # First, we'll split `l` into groups of 5 items. O(n)
    chunks = chunked(l, 5)

    # For simplicity, we can drop any chunks that aren't full. O(n)
    full_chunks = [chunk for chunk in chunks if len(chunk) == 5]


    # Next, we sort each chunk. Each group is a fixed length, so each sort
    # takes constant time. Since we have n/5 chunks, this operation
    # is also O(n)
    sorted_groups = [sorted(chunk) for chunk in full_chunks]

    # The median of each chunk is at index 2
    medians = [chunk[2] for chunk in sorted_groups]

    # It's a bit circular, but I'm about to prove that finding
    # the median of a list can be done in provably O(n).
    # Finding the median of a list of length n/5 is a subproblem of size n/5
    # and this recursive call will be accounted for in our analysis.
    # We pass pick_pivot, our current function, as the pivot builder to
    # quickselect. O(n)
    median_of_medians = quickselect_median(medians, pick_pivot)
    return median_of_medians

def chunked(l, chunk_size):
    """Split list `l` it to chunks of `chunk_size` elements."""
    return [l[i:i + chunk_size] for i in range(0, len(l), chunk_size)]