import random

matrix = []
sum_numbers = 0

for line in range(3):
    matrix_line = []
    for column in range(3):
        matrix_line.append(random.randint(10, 30))
        if line < column:
            sum_numbers += matrix_line[column]

    matrix.append(matrix_line)

print('The generated matrix is:\n')

for i in matrix:
    print(i)

print(f'\nThe sum of the numbers above the main diagonal is {sum_numbers}.')