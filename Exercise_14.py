import random

bingo_card = []
matrix_line = 5
matrix_colunm = 5

bingo_numbers = random.sample(range(0, 99), 45)
bingo_numbers.sort()

for i in range(matrix_line):
    bingo_line = []
    for j in range(matrix_colunm):
        bingo_line.append(bingo_numbers[j + 5 * i])

    bingo_card.append(bingo_line)

bingo_table = list(map(list, zip(*bingo_card)))

for i in bingo_table:
    print(i)
