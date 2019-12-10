#program to find first n fibonacci numbers
n = int(input("Enter n"))

a = 1
b = 1
c = -1
l = []
l.append(a)
l.append(b)
for i in range(n-2):
    c = a+b
    l.append(c)
    a = b
    b = c

print(l)