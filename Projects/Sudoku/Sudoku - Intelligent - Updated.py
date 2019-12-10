grid = []  # sudoku grid
possibles = {}  # maps tuple(r, c) to list of possibilities of that cell
invalid_grid = False  # keeps track of whether our current grid is invalid (unsolvable or no distinct solution)
assigned_cell = False  # keeps track of if a cell got it final value this iteration. Updated every iteration
cells_assigned_this_step = 0  # number of cells we assigned this step


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
    global assigned_cell
    global invalid_grid

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
    '''
    if len(current) == 1:  # if there's only one possibility, we fill it in as the value of that cell
        grid[i][j] = current[0]
        del possibles[(r, c)]  # also, remove that index from the dictionary since the cell is filled
        assigned_cell = True  # we assigned a cell its final value
    '''
    if len(current) == 0:  # if there are no possibilities, we have an invalid grid
        invalid_grid = True


# checks if a cell is the only one that can possibly take a value required in its row/col/block
def check_only_possible(r, c):
    global assigned_cell
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
            del possibles[(r, c)]
            assigned_cell = True
            break

        if poss not in col_leftovers:  # similarly for column
            grid[r][c] = poss
            del possibles[(r, c)]
            assigned_cell = True
            break

        if poss not in block_leftovers:  # similarly for block
            grid[r][c] = poss
            del possibles[(r, c)]
            assigned_cell = True
            break


# checks block with coordinates r,c to see if any required value can exist only in a row/col, then modify possibles
def process_of_elimination_block(r, c):
    global assigned_cell

    current_block = block(r, c)  # list of elements in given block
    required = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # list of elements that current block requires

    for num in current_block:  # for every number in this block
        if num in required:  # we don't require it, since it is already present
            required.remove(num)  # so remove from list

    mandates = {}  # dictionary from (r, c) to list containing nums that cell (r, c) must have
    # all non-mandatory values will be removed if cell has any mandates

    for num in required:  # iterating through all required numbers
        possible_cells_r = []  # list containing row coordinates of cells that can contain num
        possible_cells_c = []  # list containing col coordinates of cells that can contain num

        for i in range(r * 3, r * 3 + 3):  # iterating through all the cells in this block
            for j in range(c * 3, c * 3 + 3):
                if grid[i][j] == 0 and num in possibles[(i, j)]:  # if the cell can contain num
                    possible_cells_r.append(i)  # add the coordinates to their corresponding lists
                    possible_cells_c.append(j)

        # if the number of cells that can contain num is more than 3, they cannot all be in the same row/col
        if len(possible_cells_c) > 3:
            continue

        # set removes duplicate values. If length of set is 1, all of them have same row index (lie in same row)
        if len(set(possible_cells_r)) == 1:
            # no other cells in this row can contain num
            for i in range(9):  # iterating through the row
                # if the cell is not one of the only ones that can contain num
                if grid[possible_cells_r[0]][i] == 0 and num in possibles[(possible_cells_r[0], i)] \
                        and i not in possible_cells_c:
                    possibles[(possible_cells_r[0], i)].remove(num)  # remove num from its possibilities

                # else, we make it mandatory for the cell to have num as its possibility
                elif grid[possible_cells_r[0]][i] == 0 and num in possibles[(possible_cells_r[0], i)]:
                    if (possible_cells_r[0], i) not in list(mandates.keys()):  # if the cell isn't in the dictionary
                        mandates[(possible_cells_r[0], i)] = []  # put it there
                    mandates[(possible_cells_r[0], i)].append(num)  # and add num as an element

        elif len(set(possible_cells_c)) == 1:  # similarly if all possible cells are in the same column
            # no other cells in this col can contain num
            for i in range(9):  # iterating through the col
                # if the cell is not one of the only ones that can contain num
                if grid[i][possible_cells_c[0]] == 0 and num in possibles[(i, possible_cells_c[0])] \
                        and i not in possible_cells_r:
                    possibles[(i, possible_cells_c[0])].remove(num)  # remove num from its possibilities

                # else, we make it mandatory for the cell to have num as its possibility
                elif grid[i][possible_cells_c[0]] == 0 and num in possibles[(i, possible_cells_c[0])]:
                    if (i, possible_cells_c[0]) not in list(mandates.keys()):  # if the cell isn't in the dictionary
                        mandates[(i, possible_cells_c[0])] = []  # put it there
                    mandates[(i, possible_cells_c[0])].append(num)  # and add num as an element

        # now, we need to update possibilities of all cells which are mandated to take a value
        for cell in list(mandates.keys()):  # iterating through all the cells which now need to take mandatory values
            # we set the possibilities for the cell to be the intersection of its current probabilities with the set
            # of its mandatory values
            if len(list(set(possibles[cell]).intersection(set(mandates[cell])))) != 0:
                possibles[cell] = list(set(possibles[cell]).intersection(set(mandates[cell])))
            '''
            if len(possibles[cell]) == 1:  # if now the cell can only take one value
                grid[cell[0]][cell[1]] = possibles[cell][0]  # assign it that value
                # we need to now update all the other cells that have this value as mandatory to not have it
                for other in list(mandates.keys()):  # iterating through all cells in mandates
                    # if this cell has the current value as mandatory and isn't the cell which took the value
                    if possibles[cell][0] in mandates[other] and other != cell:
                        mandates[other].remove(possibles[cell][0])  # remove the value from its mandates
            
                del possibles[cell]  # we no longer keep track of this cell's possibilities
                assigned_cell = True
            '''


# checks entire grid for cells with only one possibility and assigns it
def check_singletons():
    global assigned_cell
    global invalid_grid

    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0 and len(possibles[(i, j)]) == 1:
                grid[i][j] = possibles[(i, j)][0]
                del possibles[(i, j)]
                assigned_cell = True
            elif grid[i][j] == 0 and len(possibles[(i, j)]) == 0:
                invalid_grid = True
                break

        if invalid_grid:
            break


# returns whether grid is unsolved i.e. contains a 0
def is_solved():
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return False

    return True


print("Enter 9x9 unsolved grid. Write 0 for a blank cell. Cells should be space separated")

for i in range(9):  # taking input
    grid.append([int(x) for x in input().split()])

for i in range(9):  # initialising possibilities for all 0s
    for j in range(9):
        if grid[i][j] == 0:
            find_possibles(i, j)

while not is_solved():  # while our grid isn't solved
    for i in range(9):  # finding possibilities for all 0s
        for j in range(9):
            if grid[i][j] == 0:  # if the cell is empty
                find_possibles(i, j)  # find its possibilities

    check_singletons()

    for i in range(3):  # iterating through all blocks
        for j in range(3):
            # it may be possible that a value required by a block can only be present in cells of a particular row/col
            # in that block. In such a case, we can reduce the possibilities of cells drastically

            process_of_elimination_block(i, j)

    check_singletons()  # check if there are cells with only one possible value and assign them that value

    if invalid_grid:  # if the grid turns out to be invalid
        print("ERR: Invalid grid")  # send an error message
        break  # stop trying to solve it

    if assigned_cell:  # if we assigned a cell its value
        assigned_cell = False  # reset
        continue  # reiterate, since we need to update the possibilities of all other cells before further checks

    for i in range(9):  # checking all cells
        for j in range(9):
            # we didn't assign a value based off of it having only one possibility, but
            # it may be the only one which can take a given value in row/col/block
            check_only_possible(i, j)

    if invalid_grid:
        print("ERR: Invalid grid")
        break

    if assigned_cell:  # if we assigned a cell its value
        assigned_cell = False  # reset
        continue  # reiterate, since we need to update the possibilities of all other cells before further checks

        # TODO: naked pairs: only boxes in a grid that can have those values so eliminate corresponding row/cols

for row in grid:
    for cell in row:
        print(cell, end=' ')
    print()
