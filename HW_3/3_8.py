"""
8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. Программа должна вычислять сумму
введенных элементов каждой строки и записывать ее в ее последнюю ячейку. В конце следует вывести полученную матрицу.
"""

# Не осилил

M = 5
N = 4
matrix = []

for i in range(N):
    row = []
    summ = 0
    print(f'{i} - я строка!!!')

    for j in range(M-1):
        num = int(input(f'Элемент {j}: '))
        summ += num
        row.append(num)

    row.append(summ)
    matrix.append(row)

for line in matrix:
    print(line)
