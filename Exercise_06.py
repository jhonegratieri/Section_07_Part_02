import random

matrix_1 = []
matrix_2 = []
matrix_greatest_numbers = []

for i in range(1, 5):
    matrix_line_1 = []
    matrix_line_2 = []

    for j in range(1, 5):
        matrix_line_1.append(random.randrange(0, 50))
        matrix_line_2.append(random.randrange(0, 50))

    matrix_1.append(matrix_line_1)
    matrix_2.append(matrix_line_2)

for i in range(4):
    matrix_line_resultant = []

    for j in range(4):
        if matrix_1[i][j] < matrix_2[i][j]:
            matrix_line_resultant.append(matrix_2[i][j])
        else:
            matrix_line_resultant.append(matrix_1[i][j])

    matrix_greatest_numbers.append(matrix_line_resultant)

print('The first generated matrix is:\n')

for a in matrix_1:
    print(a)

print('\nThe second generated matrix is:\n')

for b in matrix_2:
    print(b)

print('\nThe third generated matrix with only the highest numbers of each position of the previous matrices is:\n')

for c in matrix_greatest_numbers:
    print(c)
