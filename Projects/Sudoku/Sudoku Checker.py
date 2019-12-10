# returns list of xth column elements in grid but makes rr, cc element -1, x is 0-indexed
def colm(rr, cc, grid):
    return [grid[r][cc] if r != rr else -1 for r in range(9)]  # return list of all elements at index i in each row


# returns list containing elements in given box but makes i, j element -1, box indexes are 0-indexed from top left
def blockm(r, c, grid, i, j):
    ret = []
    for rr in range(3):
        for cc in range(3):
            ret.append(grid[r * 3 + rr][c * 3 + cc] if (r * 3 + rr, c * 3 + cc) != (i, j) else -1)
    return ret


unsol_grid = []
print("Enter 9x9 unsolved grid. Write 0 for a blank cell. Cells should be space separated")

for i in range(9):  # taking input
    unsol_grid.append([int(x) for x in input().split()])

sol_grid = []
print("Enter 9x9 solved grid. Write 0 for a blank cell. Cells should be space separated")

for i in range(9):  # taking input
    sol_grid.append([int(x) for x in input().split()])

solved = True
for i in range(9):
    for j in range(9):
        # if there is a cell where value was given but it is not the same in the answer
        if unsol_grid[i][j] != 0 and unsol_grid[i][j] != sol_grid[i][j]:
            print("ERR: Changed grid at (", i, ',', j, ')')  # print error message
            solved = False  # the grid isn't solved

        if (sol_grid[i][j] in sol_grid[i][0:j] + sol_grid[i][
                                                 j + 1:]  # if the current cell value is duplicate in its row
                or sol_grid[i][j] in colm(i, j, sol_grid)  # or it is duplicate in its column
                or sol_grid in blockm(i // 3, j // 3, sol_grid, i, j)):  # or it is duplicate in its block
            print("ERR: Repetition at (", i, ',', j, ')')  # print error message
            solved = False  # the grid isn't solved

        if not solved:
            break
    if not solved:
        break

if solved:
    print("SOLVED")
