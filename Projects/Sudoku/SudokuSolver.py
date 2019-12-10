def find_next_empty(r, c, grid):
      for j in range(c, 9):
            if(grid[r][j] == 0):
                  return r, j

      for i in range(r + 1, 9):
            for j in range(9):
                  if(grid[i][j] == 0):
                        return i, j
      return -1, -1


def find_possibilities(r, c, grid):
      l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

      for i in grid[r]:
            if(i != 0 and l.count(i) > 0):
                  l.remove(i)

      for i in range(9):
            if(grid[i][c] != 0 and l.count(grid[i][c]) > 0):
                  l.remove(grid[i][c])

      gridr = int(r / 3) * 3
      gridc = int(c / 3) * 3
      for i in range(gridr, gridr+3):
            for j in range(gridc, gridc+3):
                  if(grid[i][j] != 0 and l.count(grid[i][j]) > 0):
                        l.remove(grid[i][j])
      return l

def solve_grid(r, c, grid):
      nextr, nextc = find_next_empty(r, c, grid)

      if(nextr == -1 and nextc == -1):
            return True

      nums = find_possibilities(nextr, nextc, grid)

      for i in nums:
            grid[nextr][nextc] = i
            rr = nextr
            cc = nextc
            if(cc == 8):
                  rr = rr + 1
                  cc = 0
            else:
                  cc = cc + 1

            solvable = solve_grid(rr, cc, grid)

            if(solvable):
                  return True

      return False


grid = []
print("Enter 9x9 unsolved grid. Write 0 for a blank cell. Cells should be space separated")
for i in range(9):
      grid.append([int(x) for x in input().split()])
print(grid)
solvable = solve_grid(0, 0, grid)
print(solvable)
if(solvable):
      print(grid)