"""
Алгоритмы сортировки
Сортировка пузырьком.
Быстрая сортировка.
Сортирвока Шелла
"""

# Сортировка Пузырьком. Сложность алгоритма O(n2)
# import random

# Создание массива
# array = [i for i in range(16)]
# random.shuffle(array)
# print(array)

# array = [8, 15, 7, 13, 6, 5, 10, 1, 11, 14, 12, 4, 2, 3, 9, 0]

# n = 1
# while n < len(array):
#     for i in range(len(array) - n):   # в каждом новом цикле мы последний элемнт n уже не берем
#         if array[i] > array[i + 1]:
#             array[i], array[i + 1] = array[i + 1], array[i]
#     n += 1
#     print(array)
# print(array)
# Для домашки!!!!!! - для усложнения алгоритма, добавить проверку, что список отсортирован и не надо дальше продолжать цикл
# Добавить провекур, на одинаковые элементы
# =====================================================================================================================

# array = [8, 15, 7, 13, 6, 5, 10, 1, 11, 14, 12, 4, 2, 3, 9, 0]

# def selection_sort(array):
#     for i in range(len(array)):
#         idx_min = i
#         for j in range(i + 1, len(array)):
#             if array[j] < array[idx_min]:
#                 idx_min = j
#         array[idx_min], array[i] = array[i], array[idx_min]
#         print(array)
#
# selection_sort(array)

# =====================================================================================================================
# ЗАДАТЬ ВОПРОС - МОЖНО ЛИ РАЗБИТЬ МАССИВ НА ЧАСТИ И ПРОВОДИТЬ СОРТИРОВКУ В НИХ ДВОИХ
# array = [8, 15, 7, 13, 6, 5, 10, 1, 11, 14, 12, 4, 2, 3, 9, 0]

#
# def insertion_sort(array):
#     for i in range(1, len(array)):
#         spam = array[i]
#         j = i
#
#         while array[j - 1] > spam and j > 0:
#             array[j] = array[j - 1]
#             j -= 1
#         array[j] = spam
#         print(array)
#
# insertion_sort(array)
# =====================================================================================================================
# Алгоритм быстрой сортировки

# import random
#
# array_new = [8, 15, 7, 13, 6, 5, 10, 1, 11, 14, 12, 4, 2, 3, 9, 0]


# def quick_sort(array, fst, lst):
#     print(array)
#     if fst >= lst:
#         return
#
#     pivot = array[random.randint(fst, lst)]  # Создаем опорный элемнт, относительно которого будет проходить проверка
#     i, j = fst, lst
#
#     while i <=j:
#         while array[i] < pivot:
#             i += 1
#
#         while array[j] > pivot:
#             j -= 1
#
#         if i <= j:
#             array[i], array[j] = array[j], array[i]
#             i += 1
#             j -= 1
#
#     quick_sort(array, fst, j)
#     quick_sort(array, i, lst)
#
#
# quick_sort(array_new, 0, len(array_new) - 1)
# print(array_new)
# =====================================================================================================================
# Сортировка с использованием дополнительной памяти
# array_new = [8, 15, 7, 13, 6, 5, 10, 1, 11, 14, 12, 4, 2, 3, 9, 0]
#
#
# def quick_sort(array):
#     if len(array) <= 1:
#         return array  # Нет смысла сортировать такой массив, мы его возвращаем
#
#     pivot = random.choice(array)
#
#     s_ar = []
#     m_ar = []
#     l_ar = []
#
#     for item in array:
#         if item < pivot:
#             s_ar.append(item)
#         elif item > pivot:
#             l_ar.append(item)
#         else:
#             m_ar.append(item)
#     print(s_ar, m_ar, l_ar)
#     return quick_sort(s_ar) + m_ar + quick_sort(l_ar)
#     # Срабатывает рекурсия, маленькая и большая части идут снова на сортировку и сортируются до тех пор, пока длина массива не станет меньеш или равна 1
#
# array_super_new = quick_sort(array_new)
# print(array_super_new)

# Расход вдвое больше памяти при использовании этого алгоритма сортировки

# =====================================================================================================================
# Сортировка Шелла.
# Сортировка основанная на выборе шага между сравниваемыми элементами равный половине списка. Эти два лемента сравниваются
# При каддой последующей итерации сравнения, длинна шага меньшается в двое
# Эта сортировка для сортировки массивово до 4 тысяч элементов массива


# array_new = [8, 15, 7, 13, 6, 5, 10, 1, 11, 14, 12, 4, 2, 3, 9, 0]
#
# def shell_sort(array):
#
#     assert len(array) < 4000, 'Массив слишком большой'
#
# # Генератор - что-то возвращает  и запоминает позицию где он остановился в момент возврата
#     def new_increment(array):
#         inc = [1 ,4, 10, 23, 57, 132, 301, 701, 1750]
#         while len(array) < inc[-1]:
#             inc.pop()
#
#         while len(inc) > 0:
#             yield inc.pop()
#
#
#     for increment in new_increment(array):
#         for i in range(increment, len(array)):
#             for j in range(i, increment - 1, -increment):
#                 if array[j - increment] <=array[j]:
#                     break
#
#                 array[j], array[j - increment] = array[j - increment], array[j]
#                 print(array_new)
#
# shell_sort(array_new)
# print(array_new)

# =====================================================================================================================
# array_new = [8, 15, 7, 13, 6, 5, 10, 1, 11, 14, 12, 4, 2, 3, 9, 0]
#
#
#  class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __repr__(self):
#         return f'name: {self.name}; age: {self.age}'
#
#
# p_1 = Person('Ivan', 67)
# p_2 = Person('Kolya', 15)
# p_3 = Person('Hottabich', 365)
# p_4 = Person('Vasya', 90)
# people = [p_1, p_2, p_3, p_4]
#
# print(*people, sep='\n')
# print(*people)
# print(people)

# a = sorted(people)  # Сортировка не сработает, поскольку неопнятно сортировке как сортировать по имени или возрасту


# def by_name(person):
#     return person.name

# a = sorted(people, key = by_name)
# print(a)


# Сортировка для сложных объектов, у которых много аргументов, и надо выбирать сортировку по определенному аргументу
# from operator import attrgetter
#
# b = sorted(people, key = attrgetter('name'))
# print(b)
#
#
# с = sorted(people, key = attrgetter('name'), reverse = True)  # Для сортирвоки в обратном порядке
# print(с)
