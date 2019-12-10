#program to find factorial of a number n
n = int(input("Enter number to find factorial of"))

#0! = 1
if(n == 0):
    print("0! = 1")
else:
    factorial = 1
    n_copy = n
    while(n_copy != 1):
        factorial = factorial * n_copy
        n_copy = n_copy - 1
    print(n, '! = ', factorial)
