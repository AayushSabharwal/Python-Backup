#gradient descent

def cross(first, second):
    ans = (first[1]*second[2] - first[2]*second[1], first[2]*second[0] - first[0]*second[2], first[0]*second[1] - first[1]*second[0])
    return ans

a = float(input("a="))
b = float(input("b="))
c = float(input("c="))

normal = (a, b, c)
#surface -- ax + by + cz = 0
#gravity -z
z = (0, 0, 1)
normal2 = cross(z, normal)
dropdir = cross(normal2, normal)
print(dropdir)