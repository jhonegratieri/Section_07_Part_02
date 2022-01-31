import random

matrix = []
highest_number = -999999
highest_line_number = 0
highest_column_number = 0

for i in range(4):
    matrix_line = []

    for j in range(4):
        matrix_line.append(random.randint(0, 20))

    matrix.append(matrix_line)

for line in range(4):
    for colunm in range(4):
        if highest_number < matrix[line][colunm]:
            highest_line_number = line + 1
            highest_column_number = colunm + 1
            highest_number = matrix[line][colunm]

print(f"The generated matrix is:\n")

for i in matrix:
    print(i)

print(f"\nThe highest number in this matrix is {highest_number}\n"
      f"It is located in row {highest_line_number} column {highest_column_number}")
