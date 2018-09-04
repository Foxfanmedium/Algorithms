"""
2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со
значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 0, 3, 4, 5 (индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.
"""

# Мое решение
lst = list(input('Введите число: '))
even_index = []

for i in range(len(lst)):
    if int(lst[i]) % 2 == 0:
        even_index.append(i)
print(even_index)


# Решение с урока
#version_1
# import random
#
# SIZE = 10
# array = [random.randint(-100, 100) for _ in range(SIZE)]
# print(array)
# result = []
# for i in range(len(array)):
#     if array[i] % 2 == 0:
#         result.append(i)
# print(f'Индексы четных элементов {result}')

#version_2
# import random
# SIZE = 10
# array = [random.randint(-100, 100) for _ in range(SIZE)]
# print(array)
# result_new = [i for i in range(len(array)) if array[i] % 2 == 0]
# print(f'Индексы четных элементов {result_new}')







