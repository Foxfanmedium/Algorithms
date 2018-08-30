import random

# size = 3
# matrix = [[random.randint(1, 10) for _ in range(size)] for _ in range(size)]
# print(matrix)


# Вывод через цикл for
# for line in matrix:
#     print(line)
# print('*' * 50)

#======================================================================================================================
size = 3
matrix = [[random.randint(1, 10) for _ in range(size * 2)] for _ in range(size)]
# print(matrix)

for line in matrix:
    print(line)

print('*' * 50)

sum_column = [0] * len(matrix[0])

for line in matrix:
    sum_line = 0

    for i, item in enumerate(line):
        sum_line += item
        sum_column[i] += item

        print(f'{item: >4}', end='')

    print(f'    | {sum_line}')

print('-' * (len(matrix[0] * 5)))

for s in sum_column:
    print(f'{s: >4}', end='')



