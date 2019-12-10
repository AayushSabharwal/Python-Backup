#Q2 to print elements of matrix in spiral format

s = input()
l = []

while(len(s) > 0):
    l.append([int(x) for x in s.split(' ')])
    s = input()

n = len(l)
m = len(l[0])

dirn = ['r', 'd', 'l', 'u']
cdir = 0
ans = []
while(len(ans) < n*m):
    if(dirn[cdir] == 'r'):
        ans.extend(l[0])
        l.pop(0)
    elif(dirn[cdir] == 'd'):
        for i in range(len(l)):
            ans.append(l[i][-1])
            l[i].pop(-1)
    elif(dirn[cdir] == 'l'):
        ans.extend(l[-1][::-1])
        l.pop(-1)
    else:
        for i in range(len(l)):
            ans.append(l[len(l)-i-1][0])
            l[len(l) - i - 1].pop(0)
    cdir = (cdir + 1)%4

for i in ans:
    print(i, end = ' ')