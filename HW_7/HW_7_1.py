"""
1. Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив, заданный случайными числами на
промежутке [-100; 100). Вывести на экран исходный и отсортированный массивы.1. Отсортировать по убыванию
методом «пузырька» одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100).
Вывести на экран исходный и отсортированный массивы.
"""

"""
Решение в видуе функции.
Функция должна быть доработана чтобы работала быстрее
"""

# Version 1
import random
import numpy

array = [random.randint(-100, 100) for _ in range(20)]
print(array)
template = sorted(array)
print(template)


def bubble_sort(lst):
    n = 1
    while n < (len(array)):
        for i in range(len(array) - n):
            if (array > template) - (array < template) == 0:
                break
            elif array[i] > array[i + 1]:
                # if template == list(numpy.roll(array, i)):    # Другая попытка сравнить два списка, тоже не работает
                # if array == template:   # Попытка сравнить два списка, если они идентичны. кажется не работает
                if (array > template) - (array < template) == 0:  # это замена cmp(list_1, list_2)... должна быть
                    break
                else:
                    array[i], array[i + 1] = array[i + 1], array[i]
        n += 1
        print(array)


bubble_sort(array)

# Version 2

# def bubble_sort(lst):
#     sorted = False
#     temp = 0
#     if (len(lst) < 1):
#         return ("The list is empty")
#     while not sorted:
#         sorted = True
#         for i in range(0, len(lst) - 1):
#             if (lst[i] > lst[i + 1]):
#                 temp = lst[i]
#                 lst[i] = lst[i + 1]
#                 lst[i + 1] = temp
#                 sorted = False
#         print(lst)
#
#
# bubble_sort(array)
