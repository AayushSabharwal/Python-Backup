#program to check if given number n is prime or not
n = int(input("Enter number to check for prime"))
isPrime = True

for i in range(2, int(n/2)):
    if(n%i == 0):
        isPrime = False

if(isPrime):
    print(n, ' is prime')
else:
    print(n, ' is not prime')
