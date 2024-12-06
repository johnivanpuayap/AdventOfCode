def find_looped(starting_position, next_row, next_col, grid):
    
    curr_row, curr_col = starting_position
    
    visited = set()

    while True:
        
        visited.add((curr_row, curr_col, next_row, next_col))

        if curr_row + next_row < 0 or curr_row + next_row >= len(grid) or curr_col + next_col < 0 or curr_col + next_col >= len(grid[0]):
            break

        if grid[curr_row + next_row][curr_col + next_col] == "#":
            next_col, next_row = -next_row, next_col
        else:
            curr_row += next_row
            curr_col += next_col

        if (curr_row, curr_col, next_row, next_col) in visited:
            return True


input_data = []
positions = 0

with open('input6.txt', 'r') as file:
        input_data = file.read().splitlines()

total = 0
visited = set()
loopers = set()
grid = [list(row) for row in input_data]


starting_position = None
for i, row in enumerate(grid):
    if "^" in row:
        j = row.index("^")
        starting_position = (i, j)
    
next_row, next_col = -1, 0


for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] != ".":
            continue
        grid[i][j] = "#"
        if find_looped(starting_position, next_row, next_col, grid):
            total += 1
        grid[i][j] = "."

print(total)





