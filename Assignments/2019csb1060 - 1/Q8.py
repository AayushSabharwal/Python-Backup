#program to find area of triangle given its sides a, b, c
a = int(input("Enter side a"))
b = int(input("Enter side b"))
c = int(input("Enter side c"))

#semiperimeter
s = (a + b + c) / 2

#using Heron's formula for area
area = (s * (s-a) * (s-b) * (s-c)) ** 0.5
print('area of triangle = ', area
