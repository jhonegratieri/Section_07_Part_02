import random

matrix = []
highest_line_number = '0'
highest_column_number = '0'
X = random.randint(0, 20)

for i in range(4):
    matrix_line = []

    for j in range(4):
        matrix_line.append(random.randint(0, 20))

    matrix.append(matrix_line)

for line in range(4):
    for colunm in range(4):
        if X == matrix[line][colunm]:
            highest_line_number = line + 1
            highest_column_number = colunm + 1
            break

print(f"The generated matrix is:")

for i in matrix:
    print(i)

if highest_line_number != '0':
    print(f"\nThe number {X} is located in row {highest_line_number} column {highest_column_number}")
else:
    print(f'\nNumber {X} not found')
