"""
Написать программу, которая генерирует в указанных пользователем границах:
случайное целое число;
случайное вещественное число;
случайный символ. Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
"""

import random


#   случайное целое число
print('Случайное целое число')
num_start = int(input('Начало диапазона: '))
num_end = int(input('Конец диапазона: '))
# result = int(random.random() * (num_end - num_start + 1)) + num_start
result = random.randint(num_start, num_end)
print(result)

#   случайное вещественное число
print('Случайное вещественное число')
num_start = float(input('Начало диапазона: '))
num_end = float(input('Конец диапазона: '))
# result = random.random() * (num_end - num_start) + num_start
result = random.uniform(num_start, num_end)
print(round(result, 3))

#   случайный символ
print('Случайный символ')
num_start = ord(input('Начало диапазона: '))
num_end = ord(input('Конец диапазона: '))
# result = int(random.random() * (num_end - num_start + 1)) + num_start
result = random.randint(num_start, num_end)
print(chr(result))




# Мое первоналчальное решение
# import random
#
# limit_1 = int(input('Введите первую границу числового диапазона: '))
# limit_1_1 = int(input('Введите вторую границу числового диапазона: '))
#
# limit_2 = (input('Введите первую границу символьного диапазона: '))
# limit_2_1 = (input('Введите вторую границу символьного диапазона: '))
#
# limit_2 = ord(limit_2)
# limit_2_1 = ord(limit_2_1)
#
# integer_number = int(random.randint(limit_1, limit_1_1))
# float_number = float(random.randint(limit_1, limit_1_1))
# symbol = chr(random.randint(limit_2, limit_2_1))
#
# print(integer_number)
# print(float_number)
# print(symbol)
