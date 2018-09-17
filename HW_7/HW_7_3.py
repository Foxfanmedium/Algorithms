"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найти в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
которые не меньше медианы, в другой – не больше ее.
Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках.

Примечание:
Если брать без сортровки исходного массива, то не брать сортировки рассмотренные на уроке
и не брать сортировку методом слияния - ЭТО ХАРД
К примеру, сортировка гномов??? или коктельная сортировка
В отсортированном масииве медина лежит по середине
Numpy не использовать
"""
import random

m = random.randint(1, 10)
print('m is: ', int(m))
r = 2 * m + 1
array = [random.randint(1, 100) for _ in range(r)]
# print(array)
sorted_array = sorted(array)  # сортируем список
print(sorted_array)
len = len(sorted_array)  # находим длинну списка
index = len // 2  # хотя по идее в качестве индекса списка можно использовать и значение m
print('index is : ', index)
print('Mediana is :', sorted_array[index])
print('Mediana is :', sorted_array[m])


# Сортировка перемешиванием
# Лучший случай для этой сортировки — отсортированный массив O(n),
# худший — отсортированный в обратном порядке  O(n*n)

# left = 0
# right = len(array) - 1
#
# while left <= right:
#     for i in range(left, right, +1):
#         if array[i] > array[i + 1]:
#             array[i], array[i + 1] = array[i + 1], array[i]
#     right -= 1
#
#     for i in range(right, left, -1):
#         if array[i - 1] > array[i]:
#             array[i], array[i - 1] = array[i - 1], array[i]
#     left += 1
#
# print(array)


"""
Задачу без сортировки не осилил.  
"""

# Способ, который Вы бы назвали Python stile
# import statistics
# print(statistics.median(array))

# И способ, который Вы запретили (использование numpy)
# from numpy import median
# print(int(median(array)))
