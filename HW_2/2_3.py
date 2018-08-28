"""
3. Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран.
Например, если введено число 3486, то надо вывести число 6843.
"""

num = input('Введите число для преобразования: ')

list_numbers = []
list_revers = []

for i in num:
    list_numbers.append(int(i))

for i in reversed(list_numbers):
    list_revers.append(i)
print(''.join([str(i) for i in list_revers]))
