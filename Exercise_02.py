matrix = []

for i in range(5):
    matrix_line = []

    for j in range(5):
        if i == j:
            matrix_line.append(1)
        else:
            matrix_line.append(0)

    matrix.append(matrix_line)

print('The generated matrix is:')

for a in matrix:
    print(a)
