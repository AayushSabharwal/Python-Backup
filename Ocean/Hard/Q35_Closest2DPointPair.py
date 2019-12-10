#Closest pair of 2D points

def dist1(x, y):
    return x-y if x > y else y-x

def dist(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

def baseCase(l):
    mn = dist(l[0], l[1])
    for i in range(1, len(l)-1):
        t = dist(l[i], l[i+1])
        if(t < mn):
            mn = t
    return mn

def minDist(l):
    if(len(l) <= 3):
        return baseCase(l)
    dl = minDist(l[0:int(len(l)/2)])
    dr = minDist(l[int(len(l)/2) + 1:])
    return dl if dl < dr else dr
    
n = int(input("Enter n"))
l = []
l.append([int(input("Enter x")), int(input("Enter y"))])
mxx = l[0][0]
for i in range(1, n):
    l.append([int(input("Enter x")), int(input("Enter y"))])
    if(l[i][0] > mxx):
        mxx = l[i][0]

l.sort()

d = minDist(l)
midx = l[int(len(l)/2)][0]
middle = []
for i in range(n):
    if(dist1(l[i][0], midx) < d):
        middle.append(l[i])

middle.sort(key = lambda x : x[-1])
mnd = d
for i in range(len(middle)):
    for j in range(i+1, len(middle)):
        tmp = dist(middle[i], middle[j])
        if(tmp < mnd):
            mnd = tmp

print(min(d, mnd)**0.5)
