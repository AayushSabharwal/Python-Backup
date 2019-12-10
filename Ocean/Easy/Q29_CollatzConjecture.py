#collatz conjecture
n = int(input("Enter n"))

cycle = []
cycle.append(n)

while(n != 1):
    if(n%2 == 0):
        n = int(n/2)
    else:
        n = 3 * n + 1
    cycle.append(n)

print(cycle)
print(len(cycle))