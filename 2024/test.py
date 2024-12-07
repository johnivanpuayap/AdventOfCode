found = []
def find_loop (x, y, direction):

    print('Checking for loop at:', x, y, direction)

    if direction == 'up':
        for height in range(1, len(matrix) - x):
                for width in range(1, len(matrix) - y):

                    upper_left = (x,y, 'up')
                    upper_right = (x+1, y+width, 'right')
                    lower_right = (x+height+1, y+width-1, 'down')
                    lower_left = (x+height, y-1, 'left')
                    side1 = False
                    side2 = False
                    side3 = False

                    if upper_right in blocks:
                        side1 = True
                    if lower_right in blocks:
                        side2 = True
                    if lower_left in blocks:
                        side3 = True

                    if side1 + side2 + side3 == 2 and (upper_left, upper_right, lower_right, lower_left) not in found:
                        print('Found loop at:')
                        print(upper_left)
                        print(upper_right)
                        print(lower_right)
                        print(lower_left)
                        found.append((upper_left, upper_right, lower_right, lower_left))
                        return True
        
        return False

    elif direction == 'right':
        for height in range(1, len(matrix) - x):
                for width in range(1, len(matrix) - y):

                    upper_left = (x-1, y-width, 'up')
                    upper_right = (x, y, 'right')
                    lower_right = (x+height, y-1, 'down')
                    lower_left = (x+height-1, y-width-1, 'left')

                    side1 = False
                    side2 = False
                    side3 = False 

                    if lower_right in blocks:
                        side1 = True

                    if lower_left in blocks:
                        side2 = True

                    if upper_left in blocks:
                        side3 = True

                    if side1 + side2 + side3 == 2 and (upper_left, upper_right, lower_right, lower_left) not in found:
                        print('Found loop at:')
                        print(upper_left)
                        print(upper_right)
                        print(lower_right)
                        print(lower_left)
                        found.append((upper_left, upper_right, lower_right, lower_left))
                        return True
        
        return False
 

    elif direction == 'down':
        for height in range(1, len(matrix) - x):
                for width in range(1, len(matrix) - y):

                    upper_left = (x-height-1, y-width+1, 'up')
                    upper_right = (x-height, y+1, 'right')
                    lower_right = (x, y, 'down')
                    lower_left = (x-1, y-width, 'left')

                    side1 = False
                    side2 = False
                    side3 = False
                    
                    if lower_left in blocks:
                        side1 = True

                    if upper_left in blocks:
                        side2 = True

                    if upper_right in blocks:
                        side3 = True

                    if side1 + side2 + side3 == 2 and (upper_left, upper_right, lower_right, lower_left) not in found:
                        print('Found loop at:')
                        print(upper_left)
                        print(upper_right)
                        print(lower_right)
                        print(lower_left)
                        found.append((upper_left, upper_right, lower_right, lower_left))
                        return True
        
        return False
    else:
        for height in range(1, len(matrix) - x):
                for width in range(1, len(matrix) - y):

                    upper_left = (x-height, y+1, 'up')
                    upper_right = (x-height+1, y+width+1, 'right')
                    lower_right = (x+1, y+width, 'down')
                    lower_left= (x, y, 'left')

                    side1 = False
                    side2 = False
                    side3 = False

                    if upper_left in blocks:
                        side1 = True

                    if upper_right in blocks:
                        side2 = True

                    if lower_right in blocks:
                        side3 = True

                    if side1 + side2 + side3 == 2 and (upper_left, upper_right, lower_right, lower_left) not in found:
                        print('Found loop at:')
                        print(upper_left)
                        print(upper_right)
                        print(lower_right)
                        print(lower_left)
                        found.append((upper_left, upper_right, lower_right, lower_left))
                        return True
        
        return False


total = 0

matrix = []

with open("input6t.txt", "r") as file:
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

blocks = []

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

        blocks.append((next_x, next_y, current_direction))

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


for block in blocks:
    x = block[0]
    y = block[1]

    if find_loop(x,y, block[2]):
        total += 1
        continue


print('Number of possible loops:', total)

