matrix = []

with open("input4.txt", "r") as file:
    
    for line in file:
        matrix.append(line.strip())

num_of_xmas = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        
        if matrix[i][j] == 'A':        
            if i - 1 >= 0 and i+1 < len(matrix) and j - 1 >= 0 and j+1 < len(matrix[i]):

                diagonal_1 = False;
                diagonal_2 = False;
                
                if (matrix[i-1][j-1] == 'M' and matrix[i+1][j+1] == 'S') or ((matrix[i-1][j-1] == 'S' and matrix[i+1][j+1] == 'M')) :
                    diagonal_1 = True

                if (matrix[i-1][j+1] == 'S' and matrix[i+1][j-1] == 'M') or (matrix[i-1][j+1] == 'M' and matrix[i+1][j-1] == 'S'):
                    diagonal_2 = True
                

                if (diagonal_1 and diagonal_2):
                    num_of_xmas += 1



print("Number of XMAS found:", num_of_xmas)