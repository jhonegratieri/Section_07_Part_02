import random

matrix = []
transformed_matrix = []

for line in range(4):
    matrix_line = []
    transformed_matrix_line = []

    for column in range(4):
        matrix_line.append(random.randint(0, 20))
        if line < column:
            transformed_matrix_line.append(0)
        else:
            transformed_matrix_line.append(matrix_line[column])

    matrix.append(matrix_line)
    transformed_matrix.append(transformed_matrix_line)

print('The generated matrix is:\n')

for i in matrix:
    print(i)

print('\nThe transformed matrix is:\n')

for i in transformed_matrix:
    print(i)
