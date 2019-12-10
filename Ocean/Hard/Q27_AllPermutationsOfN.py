#program to write all permutations of n
n = int(input("Enter n"))
inp = ''
for i in range(1, n+1):
    inp = inp + str(i)
ans = []
def perm(n, i):
    if(i == len(n)-1):
        ans.append(n)
        return
    ll= len(n)
    for j in range(i, ll):
        ntmp = list(n)
        ntmp[i], ntmp[j] = ntmp[j], ntmp[i]
        ntmp = ''.join(ntmp)
        perm(ntmp, i+1)

perm(inp, 0)
print(ans)