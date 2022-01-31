matrix = []
greater_than_ten = 0

for i in range(4):
    matrix_line = []

    for j in range(4):
        matrix_line.append((i + 1) * (j + 1))

    matrix.append(matrix_line)

for line in matrix:
    print(line)
