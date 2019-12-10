#will take input and give output as a list of digits. For example, 42 would be input as 4 2 in base 10 and 3 9 in base 11
n = [int(x) for x in input().split()]
p = int(input())
q = int(input())

base10 = 0
digits = len(n)
for i in range(digits):
      base10 += n[digits - 1 - i] * p**i

n2 = []
while(base10 != 0):
      n2.append(base10%q)
      base10 = int(base10/q)

n2.reverse()

for i in n2:
      print(i, end = ' ')