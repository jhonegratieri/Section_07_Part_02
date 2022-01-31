import random

matrix = []
greater_than_ten = 0

for i in range(4):
    matrix_line = []

    for j in range(4):
        matrix_line.append(random.randint(0, 20))

        if matrix_line[j] > 10:
            greater_than_ten += 1

    matrix.append(matrix_line)

print(f'In matrix {matrix} there are {greater_than_ten} numbers greater than 10')
