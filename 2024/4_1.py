matrix = []

with open("input4.txt", "r") as file:
    for line in file:
        matrix.append(line.strip())

num_of_xmas = 0

def check_direction(i, j, di, dj):

    max_i = i + di * 3
    max_j = j + dj * 3

    if  max_i < 0 or max_i >= len(matrix) or max_j < 0 or max_j >= len(matrix[i]):
        return False

    if matrix[i + di][j + dj] == 'M' and matrix[i + 2 * di][j + 2 * dj] == 'A' and matrix[max_i][max_j] == 'S':
            return True
    
    return False

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        
        if matrix[i][j] == 'X':
           directions = [
                (-1, 0),  # Up
                (1, 0),   # Down
                (0, -1),  # Left
                (0, 1),   # Right
                (-1, -1), # Up-Left
                (-1, 1),  # Up-Right
                (1, -1),  # Down-Left
                (1, 1),   # Down-Right
            ]
           
           for di, dj in directions:
               if check_direction(i, j, di, dj):
                     num_of_xmas += 1

print("Number of XMAS found:", num_of_xmas)