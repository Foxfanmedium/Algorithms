"""
Управление памытью

Потоковое управление
Стековое управление
Управление кучей
"""

# a = 42
# print(bin(a))
# print(oct(a))
# print(hex(a))

# b = int('2a', base = 36) - перевод числа в 36-ое исчисление
# print(b)
# ======================================================================================================================
# lst = []

# lst.append(1) - добавляем в конец списка число 1
# lst.extend([2,3,4]) - расширяем список списком 2,3,4
# lst.insert(1, 5) - вставляем на первую позицию число 5

# lst.pop() - берет последний элемент и исключает его из списка, но информация о числе остается в ячейке, хоть список уже не резервиврует эту ячейку
# lst.pop() - снова исключаетс последнее число из списка, и число зарезервиррованных allocated ячеек уменьшается (было 8,с тало 6, при получившейся длине списка 3 числа)
# то есть список смотрит сколько занято, столько же резервирует ячеек


# lst.remove(5) удаление первого попавшегося значения 5 из списка, все отслаьные числа списка сдвигаются вверх после удаления 5
# allocated = 0
#
# for newsize in range(100):
#     if allocated < newsize:
#         new_allocated = (newsize >> 3) + (3 if newsize < 9 else 6)
#         allocated = newsize + new_allocated
#     print(newsize, allocated)
# ======================================================================================================================
"""
Счетчик ссылок
"""
# import sys
# a = 'Hello world!'
# print(sys.getrefcount(a)) # Получаем 4 ссылки
#
# """
# Работа Garbage collector основана на работе ссылочной схемы, которыйпроверяет ячейки
# и смотрит, есть ли в них ссылки на объекты, если нет, то они их удаляет
# """
#
# print(id(a)) - # адрес объекта в памяти

import sys

# a = 'Hello world!'

# print(sys.getsizeof(a))  # >>> 61
# print(sys.getsizeof(8))  # >>> 28

# lst = [i for i in range(10)]
# print(sys.getsizeof(lst))  # >>> 192

#
# lst = [i for i in range(10)]
#
#
# def show_size(x, level=0):
#     print('\t' * level, f'type = {x.__class__}, size = {sys.getsizeof(x)}, object = {x}')
#
#     if hasattr(x, '__iter__'):   #  Проверка что объект итерируемый
#         if hasattr(x, 'items'): # Проверка, что у объекта есть итемс
#             for y in x.items():
#                 show_size(y, level +1)
#         elif not isinstance(x, str):                    # Проверка, что это не строка, поскольку у строки тоже есть индекс. Отсеиваем бесконенчую рекурсию
#             for y in x:
#                 show_size(y, level + 1)

# show_size(lst)

 # type = <class 'list'>, size = 192, object = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	 # type = <class 'int'>, size = 24, object = 0
	 # type = <class 'int'>, size = 28, object = 1
	 # type = <class 'int'>, size = 28, object = 2
	 # type = <class 'int'>, size = 28, object = 3
	 # type = <class 'int'>, size = 28, object = 4
	 # type = <class 'int'>, size = 28, object = 5
	 # type = <class 'int'>, size = 28, object = 6
	 # type = <class 'int'>, size = 28, object = 7
	 # type = <class 'int'>, size = 28, object = 8
	 # type = <class 'int'>, size = 28, object = 9


# show_size(tuple(lst))

 # type = <class 'tuple'>, size = 128, object = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9) размер кортежа меньше, поскольку он занимает только ту память, которая необходима
	#  type = <class 'int'>, size = 24, object = 0
	#  type = <class 'int'>, size = 28, object = 1
	#  type = <class 'int'>, size = 28, object = 2
	#  type = <class 'int'>, size = 28, object = 3
	#  type = <class 'int'>, size = 28, object = 4
	#  type = <class 'int'>, size = 28, object = 5
	#  type = <class 'int'>, size = 28, object = 6
	#  type = <class 'int'>, size = 28, object = 7
	#  type = <class 'int'>, size = 28, object = 8
	#  type = <class 'int'>, size = 28, object = 9



# show_size(set(lst))
 # type = <class 'set'>, size = 736, object = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	#  type = <class 'int'>, size = 24, object = 0
	#  type = <class 'int'>, size = 28, object = 1
	#  type = <class 'int'>, size = 28, object = 2
	#  type = <class 'int'>, size = 28, object = 3
	#  type = <class 'int'>, size = 28, object = 4
	#  type = <class 'int'>, size = 28, object = 5
	#  type = <class 'int'>, size = 28, object = 6
	#  type = <class 'int'>, size = 28, object = 7
	#  type = <class 'int'>, size = 28, object = 8
	#  type = <class 'int'>, size = 28, object = 9

# d = {str(i):i for i in range(10)}
# show_size(d)


 # type = <class 'dict'>, size = 368, object = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
	#  type = <class 'tuple'>, size = 64, object = ('0', 0)
	# 	 type = <class 'str'>, size = 50, object = 0
	# 	 type = <class 'int'>, size = 24, object = 0
	#  type = <class 'tuple'>, size = 64, object = ('1', 1)
	# 	 type = <class 'str'>, size = 50, object = 1
	# 	 type = <class 'int'>, size = 28, object = 1
	#  type = <class 'tuple'>, size = 64, object = ('2', 2)
	# 	 type = <class 'str'>, size = 50, object = 2
	# 	 type = <class 'int'>, size = 28, object = 2
	#  type = <class 'tuple'>, size = 64, object = ('3', 3)
	# 	 type = <class 'str'>, size = 50, object = 3
	# 	 type = <class 'int'>, size = 28, object = 3
	#  type = <class 'tuple'>, size = 64, object = ('4', 4)
	# 	 type = <class 'str'>, size = 50, object = 4
	# 	 type = <class 'int'>, size = 28, object = 4
	#  type = <class 'tuple'>, size = 64, object = ('5', 5)
	# 	 type = <class 'str'>, size = 50, object = 5
	# 	 type = <class 'int'>, size = 28, object = 5
	#  type = <class 'tuple'>, size = 64, object = ('6', 6)
	# 	 type = <class 'str'>, size = 50, object = 6
	# 	 type = <class 'int'>, size = 28, object = 6
	#  type = <class 'tuple'>, size = 64, object = ('7', 7)
	# 	 type = <class 'str'>, size = 50, object = 7
	# 	 type = <class 'int'>, size = 28, object = 7
	#  type = <class 'tuple'>, size = 64, object = ('8', 8)
	# 	 type = <class 'str'>, size = 50, object = 8
	# 	 type = <class 'int'>, size = 28, object = 8
	#  type = <class 'tuple'>, size = 64, object = ('9', 9)
	# 	 type = <class 'str'>, size = 50, object = 9
	# 	 type = <class 'int'>, size = 28, object = 9


# show_size(frozenset(lst))
 # type = <class 'frozenset'>, size = 736, object = frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9})
	#  type = <class 'int'>, size = 24, object = 0
	#  type = <class 'int'>, size = 28, object = 1
	#  type = <class 'int'>, size = 28, object = 2
	#  type = <class 'int'>, size = 28, object = 3
	#  type = <class 'int'>, size = 28, object = 4
	#  type = <class 'int'>, size = 28, object = 5
	#  type = <class 'int'>, size = 28, object = 6
	#  type = <class 'int'>, size = 28, object = 7
	#  type = <class 'int'>, size = 28, object = 8
	#  type = <class 'int'>, size = 28, object = 9

# ======================================================================================================================

import sys
import ctypes
import struct

a = 42

print(id(a))              #>>> 1759081216
print(sys.getsizeof(a))   #>>> 28

print(ctypes.string_at(id(a), sys.getsizeof(a))) # покажи как строку
# >>> b'\x07\x00\x00\x00\x00\x00\x00\x00\xe0\x99\xd2h\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00*\x00\x00\x00'

print(struct.unpack('LLLLLLl', ctypes.string_at(id(a), sys.getsizeof(a))))
# >>> (7, 0, 1758632416, 0, 1, 0, 42) где 7 - счетчик ссылок

print(id(int))
# >>> 1758632416 - по этому адресу лежит объект целочисленный
















