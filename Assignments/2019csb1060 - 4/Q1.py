#Q1 To generate specified matrix and number cells from 1 in row wise manner
r, c = [int(x) for x in input().split(" ")]

mat = []
for i in range(r):
    mat.append([])
    for j in range(c):
        mat[i].append(0)

for i  in range(r):
    for j in range(c):
        mat[i][j] = c*i+j+1

for i in range(r):
    s = ''
    for j in range(c):
        s = s + str(mat[i][j]) + ' '
    print(s[:-1])

