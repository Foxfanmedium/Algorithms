"""
Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
"""

# print(ord('a'))
first = ord(input('1-я буква: '))
second = ord(input('2-я буква: '))
first = first - ord('a') + 1
second = second - ord('a') + 1
print(f'Порядковый номер 1-й буквы = {first}, 2-й = {second}')
print(f'Число букв между введёнными: {abs(first - second) - 1}')

list_1 = ['a', 'b']

# import string
#
# a = string.ascii_lowercase
# b = string.ascii_uppercase
# print(type(a))
# print(type(b))
# print(a)
# print(b)

