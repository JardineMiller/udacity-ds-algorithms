correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]
               

# invert the grid so we can treat columns and rows the same
def invert_grid(grid):
  new_grid = []

  for i in range(0, len(grid)):
    new_grid.append([])

  for row in grid:
    col_index = 0
    for num in row:
      new_grid[col_index].append(num)
      col_index += 1

  return new_grid

# check whether the provided row/col is valid
def validate(nums_list):
  n = len(nums_list) + 1
  nums = list(range(1, n))
  for num in nums_list:
    if num not in nums:
      return False

    nums.remove(num)
  return True

# check whether the sudoku grid is valid
def check_sudoku(grid):
    for row in grid:
      if (not validate(row)):
        return False

    inverted_grid = invert_grid(grid)

    for col in inverted_grid:
      if (not validate(col)):
        return False


    return True

print(check_sudoku(correct))
print(check_sudoku(incorrect))
print(check_sudoku(incorrect2))
print(check_sudoku(incorrect3))
print(check_sudoku(incorrect4))
print(check_sudoku(incorrect5))
