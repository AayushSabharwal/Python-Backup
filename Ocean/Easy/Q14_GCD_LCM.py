#program to find gdc and lcm of two numbers
a = int(input("Enter a"))
b = int(input("Enter b"))

if(a > b):
    a, b = b, a

l = []
for i in range(2, a):
    if(a%i == 0):
        l.append(i)

lenL = len(l)
gcd = 1
for i in range(lenL):
    if(b%l[i] == 0):
        gcd = l[i]

lcm = int(a * b / gcd)
print('gcd = ', gcd)
print('lcm = ', lcm)
