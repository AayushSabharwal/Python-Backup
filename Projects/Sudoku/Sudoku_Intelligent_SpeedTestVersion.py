grid = []  # sudoku grid
possibles = {}  # maps tuple(r, c) to list of possibilities of that cell


# returns list of xth column elements in grid, x is 0-indexed
def col(x):
    return [grid[r][x] for r in range(9)]  # return list of all elements at index i in each row


# returns list containing elements in given box, box indexes are 0-indexed from top left
def block(r, c):
    ret = []
    for rr in range(3):
        for cc in range(3):
            ret.append(grid[r * 3 + rr][c * 3 + cc])
    return ret


# returns a list of possible entries in given cell
def find_possibles(r, c):

    if grid[r][c] != 0:  # we should be checking for possibilities in an empty cell
        print("ERR: Non-empty cell check (", r, ',', c, ')')
        return

    current = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # all the possibilities
    for num in grid[r]:  # checking against elements in row
        if num in current:
            current.remove(num)

    for num in col(c):  # checking against elements in column
        if num in current:
            current.remove(num)

    for num in block(r // 3, c // 3):  # checking against elements in block, r//3,c//3 gives block indices
        if num in current:
            current.remove(num)

    possibles[(r, c)] = current  # assigning the possibility of given cell in dict


# given a cell, function updates possibilities of all cells in its row, col and block
def update_affected_cells(r, c):
    updated = []  # list of cells we have already updated, so they aren't updated extra times

    for i in range(c):  # updating row
        if grid[r][i] == 0 and i != c:
            find_possibles(r, i)
            updated.append((r, i))

    for i in range(r):  # updating column
        if grid[i][c] == 0 and i != r:
            find_possibles(i, c)
            updated.append((i, c))

    for i in range(r // 3 * 3, r // 3 * 3 + 3):  # updating block
        for j in range(c // 3 * 3, c // 3 * 3 + 3):
            if grid[i][j] == 0 and i != r and j != c and (i, j) not in updated:
                find_possibles(i, j)
                updated.append((i, j))


# checks if a cell is the only one that can possibly take a value required in its row/col/block
def check_only_possible(r, c):
    assigned_cell = False   # if we assigned this cell a value, we want to update the cells it affects

    row_leftovers = []  # elements we need in this row
    for i in range(9):
        if grid[r][i] == 0 and i != c:
            row_leftovers.extend(possibles[(r, i)])

    col_leftovers = []  # elements we need in this column
    for j in range(9):
        if grid[j][c] == 0 and j != r:
            col_leftovers.extend(possibles[(j, c)])

    block_leftovers = []  # elements we need in this block
    for i in range(r // 3 * 3, r // 3 * 3 + 3):
        for j in range(c // 3 * 3, c // 3 * 3 + 3):
            if grid[i][j] == 0 and (i, j) != (r, c):
                block_leftovers.extend(possibles[(i, j)])

    for poss in possibles[(r, c)]:  # considering each value the current cell can take
        if poss not in row_leftovers:  # if this value cannot be taken by any other cell in the row
            grid[r][c] = poss  # current cell takes this value
            assigned_cell = True
            break

        if poss not in col_leftovers:  # similarly for column
            grid[r][c] = poss
            assigned_cell = True
            break

        if poss not in block_leftovers:  # similarly for block
            grid[r][c] = poss
            assigned_cell = True
            break

    if assigned_cell:
        del possibles[(r, c)]
        update_affected_cells(r, c)


# returns whether grid is unsolved i.e. contains a 0
def is_solved():
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return False

    return True


# checks entire grid for cells with only one possibility and assigns it
def check_singletons():\

    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0 and len(possibles[(i, j)]) == 1:
                grid[i][j] = possibles[(i, j)][0]
                del possibles[(i, j)]
                update_affected_cells(i, j)


def solve(g):
    global grid
    grid = g
    n_iters = 0  # to keep track of number of times the loop has run, to prevent infinite loops

    while not is_solved() and n_iters < 200:  # while our grid isn't solved
        n_iters += 1

        for i in range(9):  # finding possibilities for all 0s
            for j in range(9):
                if grid[i][j] == 0:  # if the cell is empty
                    find_possibles(i, j)  # find its possibilities

        check_singletons()  # check if any cells can take only one value

        for i in range(9):  # checking all cells
            for j in range(9):
                if grid[i][j] == 0:
                    # we didn't assign a value based off of it having only one possibility, but
                    # it may be the only one which can take a given value in row/col/block
                    check_only_possible(i, j)

    for row in grid:
        for cell in row:
            print(cell, end=' ')
        print()
