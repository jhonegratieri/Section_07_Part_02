import random

matrix_numbers = []
sum_list = [0, 0, 0]

for i in range(3):
    child_list = []

    for j in range(3):
        child_list.append(random.randint(-20, 20))

        if j == 0:
            sum_list[0] += child_list[0]
        elif j == 1:
            sum_list[1] += child_list[1]
        else:
            sum_list[2] += child_list[2]

    matrix_numbers.append(child_list)

print('The matrix numbers is:')
for i in matrix_numbers:
    print(i)

print(f'\nThe sum of the numbers in each column is {sum_list}')
