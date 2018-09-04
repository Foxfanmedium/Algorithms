"""
1. Проанализировать скорость и сложность одного - трёх любых алгоритмов, разработанных в
рамках домашнего задания первых трех уроков.
Примечание: Результаты анализа сохранить в виде комментариев в файле с кодом.
"""

# ПРОВЕДЕНИЕ АНАЛИЗА СЛОЖНОСТИ ПЕРВОЙ ЗАДАЧИ


# Мой вариант ДЗ. Ваш комментарий был "Отлично. Но можно обойтись и без списков. Зачем память тратить впустую"
# Думаю есть что проанализировать. Потом сравню с решением, которое было разобрано на уроке.
# Интересно наглядные цифры и результаты посмотреть
"""
# import cProfile # библиотека для анализа функций
cProfile.run('main()') передаем функцию 
"""
import time
import timeit  # модуль для анализа скорости выполнения функций
import cProfile
from typing import List


# def odd_even(num):
#     start = time.time()
#     list_numbers = list()
#     odds_numbers = list()
#     evens_numbers = list()
#     list_ = list(str(num))
#     for i in list_:
#         list_numbers.append(int(i))
#     for i in list_numbers:
#         if i % 2 == 0:
#             evens_numbers.append(i)
#         else:
#             odds_numbers.append(i)
#     print(len(evens_numbers))
#     print(len(odds_numbers))
#     print(time.time() - start)


# cProfile.run('odd_even(1235678915681786635385476479562346592345676342957623465834657268952659848532659843)')
#          175 function calls in 0.000 seconds
#    Ordered by: standard name
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 1.py:20(odd_even)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         3    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#         2    0.000    0.000    0.000    0.000 {built-in method time.time}
#       164    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run(
#     'odd_even(123567891568178663538547647956234659234567634295762346583465726895265984853265984367129586348767589234859635823496523965823)')
#       257 function calls in 0.000 seconds
# Ordered by: standard name
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 1.py:21(odd_even)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      3    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#      2    0.000    0.000    0.000    0.000 {built-in method time.time}
#    246    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
ВЫВОД:
Похоже на то, что выше привведенная функция и алгоритм в ней очень простые, потому что скорость выполнения расчетов
стремиться к нулю даже при очень больших значениях. Скорее всего здесь линейная сложность О(n).
"""


"""
Оригинальный код без функции который был в ДЗ к уроку 2
num = list(input('Введите несколько цифр натурального числа: '))
list_numbers = list()
odds_numbers = list()
evens_numbers = list()

for i in num:
    list_numbers.append(int(i))

for i in list_numbers:
    if i % 2 == 0:
        evens_numbers.append(i)
    else:
        odds_numbers.append(i)
print(len(evens_numbers))
print(len(odds_numbers))
delta = time.time() - start
print(delta)
"""

#=====================================================================================================================


# ПРОВЕДЕНИЕ АНАЛИЗА СЛОЖНОСТИ ВТОРОЙ ЗАДАЧИ
# Буду брать Вашу задачу из третьей лекции 3_9(Найти максимальный элемент среди минимальных элементов столбцов матрицы)
# Ниже указано оригинальное (Ваше) решение задачи



import random
import cProfile

def create_matrix(size):
    start = time.time()
    matrix = [[random.randint(0, 100) for _ in range(size)] for _ in range(size)]
    for line in matrix:
        print(*line, sep='\t')
    max_=matrix[0][0]
    for j in range(size):
        min_ = matrix[0][j]

        for i in range(size):
            if matrix[i][j] < min_:
                min_=matrix[i][j]
        if min_ > max_:
            max_ = min_
    print(f'Max in min = {max_}')
    print(time.time() - start)

# cProfile.run('create_matrix(10)')
#       543 function calls in 0.001 seconds
# Ordered by: standard name
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 1.py:104(create_matrix)
#      1    0.000    0.000    0.000    0.000 1.py:106(<listcomp>)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#    100    0.000    0.000    0.000    0.000 random.py:173(randrange)
#    100    0.000    0.000    0.000    0.000 random.py:217(randint)
#    100    0.000    0.000    0.000    0.000 random.py:223(_randbelow)
#      1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#     12    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#      2    0.000    0.000    0.000    0.000 {built-in method time.time}
#    100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    124    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# cProfile.run('create_matrix(50)')
#       13264 function calls in 0.011 seconds
# Ordered by: standard name
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.012    0.012 1.py:104(create_matrix)
#      1    0.000    0.000    0.005    0.005 1.py:106(<listcomp>)
#      1    0.000    0.000    0.012    0.012 <string>:1(<module>)
#   2500    0.002    0.000    0.003    0.000 random.py:173(randrange)
#   2500    0.001    0.000    0.004    0.000 random.py:217(randint)
#   2500    0.001    0.000    0.002    0.000 random.py:223(_randbelow)
#      1    0.000    0.000    0.012    0.012 {built-in method builtins.exec}
#     52    0.006    0.000    0.006    0.000 {built-in method builtins.print}
#      2    0.000    0.000    0.000    0.000 {built-in method time.time}
#   2500    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#   3205    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# cProfile.run('create_matrix(100)')
#      52820 function calls in 0.030 seconds
# Ordered by: standard name
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.001    0.001    0.032    0.032 1.py:104(create_matrix)
#     1    0.000    0.000    0.019    0.019 1.py:106(<listcomp>)
#     1    0.000    0.000    0.032    0.032 <string>:1(<module>)
# 10000    0.006    0.000    0.013    0.000 random.py:173(randrange)
# 10000    0.003    0.000    0.016    0.000 random.py:217(randint)
# 10000    0.005    0.000    0.007    0.000 random.py:223(_randbelow)
#     1    0.000    0.000    0.032    0.032 {built-in method builtins.exec}
#   102    0.013    0.000    0.013    0.000 {built-in method builtins.print}
#     2    0.000    0.000    0.000    0.000 {built-in method time.time}
# 10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# 12711    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}


"""
ВЫВОД:
Делая вывод после анализа сложности данной функции можно сказать, что здесь линейная сложность O(n)
и скорость выполнения расчетов растет линейно. 
"""

# Оригинальное решение задачи 3_9
# import random
# SIZE = 5
# matrix = [[random.randint(0, 100) for _ in range(SIZE)] for _ in range(SIZE)]
# for line in matrix:
#     print(*line, sep='\t')
# max_=matrix[0][0]
# for j in range(SIZE):
#     min_ = matrix[0][j]
#
#     for i in range(SIZE):
#         if matrix[i][j] < min_:
#             min_=matrix[i][j]
#     if min_ > max_:
#         max_ = min_
# print(f'Max in min = {max_}')

#=====================================================================================================================