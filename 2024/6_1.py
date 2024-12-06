matrix = []

with open("input6.txt", "r") as file:
    for line in file:
        matrix.append(line.strip())

# Find the guard's position

starting_x = -1
starting_y = -1

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == '^':
            starting_x = i
            starting_y = j
            break
        
unique_positions = dict()


current_x = starting_x
current_y = starting_y
current_direction = 'up'
unique_positions[(current_x, current_y)] = 1

while True:    
    next_x = current_x
    next_y = current_y

    if current_direction == 'up':
        next_x -= 1
    elif current_direction == 'down':
        next_x += 1
    elif current_direction == 'left':
        next_y -= 1    
    else:
        next_y += 1

    if next_x < 0 or next_x >= len(matrix) or next_y < 0 or next_y >= len(matrix[next_x]):
        break
    
    if matrix[next_x][next_y] == '.' or matrix[next_x][next_y] == '^':
        current_x = next_x
        current_y = next_y

    elif matrix[next_x][next_y] == '#':
        if current_direction == 'up':
            current_direction = 'right'
            current_y += 1

        elif current_direction == 'right':
            current_direction = 'down'
            current_x += 1
        elif current_direction == 'down':
            current_direction = 'left'
            current_y -= 1
        else:
            current_direction = 'up'
            current_x -= 1

       
    if (unique_positions.get((current_x, current_y)) == None):
            unique_positions[(current_x, current_y)] = 1 

print("Number of unique positions visited by the guard:", len(unique_positions))