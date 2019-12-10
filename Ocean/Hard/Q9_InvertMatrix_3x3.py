#program to invert a 3x3 matrix
#http://sccilabs.org/gel103/index.php/Ocean

import numpy as np
def det3x3(arr):
    ans = arr[0,0] * (arr[1,1] * arr[2,2] - arr[1,2] * arr[2,1])
    ans = ans - arr[0,1] * (arr[1,0] * arr[2,2] - arr[1,2] * arr[2,0])
    ans = ans + arr[0,2] * (arr[1,0] * arr[2,1] - arr[1,1] * arr[2,0])
    return ans

def trace(arr):
    ans = 0
    for i in range(3):
        ans = ans + arr[i,i]
    return ans

arr = np.matrix([[1,0,1], [1,0,0], [2,1,1]])
for i in range(3):
    for j in range(3):
        arr[i,j] = int(input("Enter element"))

t = trace(arr)
t2 = trace(arr * arr)
inv = (arr * arr - arr*t + 0.5*(t*t - t2)*np.identity(3))/det3x3(arr)
print(inv)