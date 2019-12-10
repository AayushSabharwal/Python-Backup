from matplotlib import pyplot as plt
import time

# returns list containing elements in given column of grid g
def col(x, g):
    return [g[r][x] for r in range(9)]  # return list of all elements at index i in each row


# returns list containing elements in given box of grid g, box indexes are 0-indexed from top left
def block(r, c, g):
    ret = []
    for rr in range(3):
        for cc in range(3):
            ret.append(g[r * 3 + rr][c * 3 + cc])
    return ret


# check if it is possible to put i in (r, c) cell of grid g
def is_possible(r, c, g, i):
    if i in g[r]:  # if i exists in the row
        return False

    if i in col(c, g):  # or in the column
        return False

    if i in block(r // 3, c // 3, g):  # or in the block
        return False  # it isn't possible to put it here

    return True  # it isn't in row/col/block so it is possible for i to be here


# prints grid
def pretty_print_grid(g):
    for i in range(9):
        for j in range(9):
            print(g[i][j], end=' ')
        print()


# given an unsolved grid g and a list of coordinates of empty cells, this function returns whether grid is solvable
# and solves it
def fill(g, empty):
    if len(empty) == 0:  # if we have no empty cells, we have assigned every cell a valid value
        #pretty_print_grid(g)  # print the finished grid
        return True  # this grid is solvable

    for i in range(1, 10):  # iterating through 1 to 9
        if is_possible(empty[0][0], empty[0][1], g, i):  # if it is possible for i to be in this position
            g[empty[0][0]][empty[0][1]] = i  # assign it here
            if fill(g, empty[1:]):  # if solving the resultant grid with this one less empty cell is possible
                return True  # this grid is solvable
        g[empty[0][0]][empty[0][1]] = 0  # making cell empty again, in case it was assigned before but didn't lead to
        # a solution

    return False  # if we reached here, we have tried all the numbers from 1 to 9 and none resulted in a solution,
    # so the grid is unsolvable in its current state


def solve(grid):
    # to store coordinates of all empty cells in grid
    empty = []
    for row in range(9):
        for column in range(9):
            if grid[row][column] == 0:
                empty.append((row, column))

    ans = fill(grid, empty)

    if not ans:  # if we couldn't solve the grid
        print("Grid is unsolvable")

grids = []

f = open("grids.txt", "r")
raw = f.readlines()
f.close()

for i in range(len(raw)):
    if i % 9 == 0:
        grids.append([])

    grids[i // 9].append([int(x) for x in raw[i].split()])


x = list(range(len(grids)))
times = []
for i in range(len(grids)):
    start = time.time()
    a = solve(grids[i])
    end = time.time()
    if not a:
          pretty_print_grid(grids[i])
          print("!", i)
    times.append(end - start)

plt.plot(x, times)
