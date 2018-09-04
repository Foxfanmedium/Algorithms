"""
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""
# Мое решение
import random
SIZE = 10
lst = [random.randint(-200, 0) for _ in range(SIZE)]
print(lst)

max_min = -200
index = -1

for i in lst:
    if i > max_min:
        max_min = i
print(max_min)
index = lst.index(max_min)
print(f'Максимальный отрицательный элемент {max_min} и его позиция {index}')


import random

# SIZE = 10
# array = [random.randint(-1000, -800) for _ in range(SIZE)]
# print(array)

# Version_1
# i = 0
# index = -1
#
# while i < SIZE:
#     if array[i] < 0 and index == -1:
#         index = 1
#     elif array[i] < 0 and array[i] > array[index]:
#         index = i
#     i += 1
# print(f'Число {array[index]} на позиции {index}')

#--------------------------------------------------------
# Version_2

# num = float('-inf')
# index = -1
# for i, item in enumerate(array):
#     if 0 > item > num:
#         num = item
#         index = i
# print(f'Число {num} на позиции {index}')















