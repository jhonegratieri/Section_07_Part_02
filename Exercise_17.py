import random

students_matrix = []
students_lowest_score_1st_test = 0
students_lowest_score_2nd_test = 0
students_lowest_score_3rd_test = 0

for i in range(10):
    student_grades = []

    for j in range(3):
        student_grades.append(random.randint(0, 10))

    students_matrix.append(student_grades)

    if student_grades.index(min(student_grades)) == 0:
        students_lowest_score_1st_test += 1

    elif student_grades.index(min(student_grades)) == 1:
        students_lowest_score_2nd_test += 1

    else:
        students_lowest_score_3rd_test += 1

for i in students_matrix:
    print(i)

print(f'\n{students_lowest_score_1st_test} students had the lowest score on the first test, '
      f'{students_lowest_score_2nd_test} on second test and '
      f'{students_lowest_score_3rd_test} on the third test.')
