#program to input integer n in base p, convert to base q
p = int(input("Enter base of n"))
q = int(input("Enter base to convert to"))
n = int(input("Enter n"))

base10 = 0
place = 0
while(n != 0):
    base10 = base10 + (n%10)*(p**place)
    n = int(n/10)
    place = place + 1
print(base10)

conv = '\0'
while(base10 != 0):
    conv = conv + str(base10%q)
    base10 = int(base10/q)

ans = '\0'
l = len(conv)
for c in range(l):
    ans = ans + conv[l-c-1]
print(ans)