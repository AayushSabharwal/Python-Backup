#program to find smallest k digit number divisible by x
k = int(input("Enter number of digits"))
x = int(input("Enter x"))

#smallest k digit number is 10^k
num = 10**(k-1)
#if a%b = r, then a+b-r is first number after a divisible by b
r = num%x
num = num + x - r
print('smallest ', k, 'digit number divisible by ', x, ' is ', num)
