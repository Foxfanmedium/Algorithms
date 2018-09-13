import random

list_1 = [1, 2, 3, 4]
list_2 = [1, 2, 3, 4]
list_3 = [1, 2, 3, 4]
list_4 = [1, 2, 3, 4]


# for i, item in enumerate(list_1):
#     del item
#
# print(list_1)
# >>> [1, 2, 3, 4] - в данном случае происходит разрыв между индексами элементов и элементами
#-------------------------------------------
# for i, item in enumerate(list_2):
#     list_2.remove(item)
#
# print(list_2)
# >>> [2, 4] При удалении первого элемента, элементы смещаются и мы пропускаем смещенные элемент для удаления

# for i, item in enumerate(list_3):
#     list_3.pop(i)
#
# print(list_3)
#------------------------------------------------------

# for i, item in enumerate(list_4[:]):
#     list_4.remove(item)
# print(list_4)
# # >>> []
#---------------------------------------------------------

# row = [''] * 3
# board = [row] * 3
# print(board)
# board[0][0] = 'x'
# print(board)
# >>> [['x', '', ''], ['x', '', ''], ['x', '', '']]

# board = [[''] * 3 for _ in range(3)]
# print(board)


#--------------------------------------------------------

# a = [1,2,3]
# b = a
# a = a + [5,6]
# print(a, b, sep='\n')

# >>> [1, 2, 3, 5, 6]
# >>> [1, 2, 3]


# a = [1,2,3]
# b = a
# a += [5,6]
# print(a, b, sep='\n')

# >>> [1, 2, 3, 5, 6]
# >>> [1, 2, 3, 5, 6]
# ======================================================================================================================

    # t = ('one', 'two')
    # for i in t:
    #     print(i)

# >>> one
# >>> two

# t = ('one')
# for i in t:
#     print(i)
# >>> o
# >>> n
# >>> e

# t = ('one',)
# for i in t:
#     print(i)
# >>> one

# a = [1, 2, 3, 4, 5]
# print(a)
#>>> [1, 2, 3, 4, 5]


# a = [1, 2, 3, 4, 5]
# print(*a)
#>>> 1 2 3 4 5

# ======================================================================================================================

"""
Двоичный бинарный поиск в массиве
Он может проводиться только в отсортированном массиве
"""
# import random
#
# size = 10
# limit = 20
#
# array = [random.randint(0, limit) for _ in range(size)]
#
# array.sort()
# print(array)
# find = int(input('Введите число для поиска: '))
#
# pos = len(array) // 2
# left = 0
# right = len(array) - 1

# while array[pos] != find and left <= right:
#     if find > array[pos]:
#         left = pos + 1
#
#     else:
#         right = pos - 1
#     pos = (left + right) // 2
#
# print('Элемент отсутствует' if left > right else f'Позиция элемента {pos}')
# ======================================================================================================================

# import random

# size = 10
# limit = 20
# array = [random.randint(0, limit) for _ in range(size)]
# print(array)
#
# num = int(input('Введите число для вставки: '))
# pos = int(input('Введите позицию для вставки: '))
#
# array.append(None)
# i = len(array) - 1
#
# while i > pos:
#     print(array)
#     array[i], array[i -1] = array[i -1], array[i]
#     i -= 1
#
# array[pos] = num
# print(array)

# ======================================================================================================================
# size = 3
# matrix = [[random.randint(1, 10) for _ in range(size)] for _ in range(size)]
# print(matrix)


# Вывод через цикл for
# for line in matrix:
#     print(line)
# print('*' * 50)

# ======================================================================================================================
# size = 3
# matrix = [[random.randint(1, 10) for _ in range(size * 2)] for _ in range(size)]
# # print(matrix)
#
# for line in matrix:
#     print(line)
#
# print('*' * 50)
#
# sum_column = [0] * len(matrix[0])
#
# for line in matrix:
#     sum_line = 0
#
#     for i, item in enumerate(line):
#         sum_line += item
#         sum_column[i] += item
#
#         print(f'{item: >4}', end='')
#
#     print(f'    | {sum_line}')
#
# print('-' * (len(matrix[0] * 5)))
#
# for s in sum_column:
#     print(f'{s: >4}', end='')
