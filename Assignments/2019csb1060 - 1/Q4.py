 #program to find the kth largest element in a list

#size of list is n
n = int(input("Enter size of list"))
l = []
for i in range(n):
    l.append(int(input("Enter element")))
k = int(input("Enter k"))
#first we find minimum element
min = l[0]
for i in range(n):
    if(l[i] < min):
        min = l[i]

#next we find the largest element, and remove it by replacing with min
#if we repeat this, the next largest is the 2nd largest elements
#hence, we repeat this k-1 times, then the largest element is kth largest
for i in range(k-1):
    mx = l[0]   #current largest element
    ind = 0     #index of current largest element in list
    for j in range(n):
        if(mx < l[j]):
            mx = l[j]
            ind = j
    l[ind] = min

mx = l[0]
for i in range(n):
    if(l[i] > mx):
        mx = l[i]

print(k,'th largest element in list is ', mx)
