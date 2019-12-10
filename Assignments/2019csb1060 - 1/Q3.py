#program to find largest number in a list

#n is number of elements in list
n = int(input("Enter size of list"))
l = []
for i in range(n):
    l.append(int(input("Enter element of list")))

#mx stores the maximum value in list. We assume it to be l[0] initially
mx = l[0]
for i in range(n):
    if(l[i] > mx):
        mx = l[i]
print('maximum element in list = ', mx)
