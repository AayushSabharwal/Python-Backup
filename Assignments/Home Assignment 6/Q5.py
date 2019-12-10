#takes input of number of disks, rod where they are initially and rod where they end at, assuming 3 rods numbered 0, 1, 2
#gives output as space separated tuples, where each tuple (a, b) denotes topmost disk of rod a moving to rod b

def hanoi(n, start, end, other):
      if(n == 1):
            return [(start, end)]
      
      return hanoi(n-1, start, other, end) + [(start, end)] + hanoi(n-1, other, end, start)

n = int(input())
start = int(input())
end = int(input())
print(hanoi(n, start, end, 3-start-end))