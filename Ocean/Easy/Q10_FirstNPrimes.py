#program to find first n primes
#http://sccilabs.org/gel103/index.php/Ocean

n = int(input("Enter n"))
count = 0
for i in range(2, n*n):
    if(i/2 < 2):
        print(i)
        count = count + 1
    else:
        isPrime = True
        for j in range(2, int(i/2)+1):
            if(i%j == 0):
                isPrime = False
                break
        if isPrime == True:
            print(i)
            count = count + 1
    if(count == n):
        break
