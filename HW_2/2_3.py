"""
3. Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран.
Например, если введено число 3486, то надо вывести число 6843.
"""

# Version_1 - для случаев работы с целыми числами
num = int(input('Введите целое число: '))
result = 0
while num > 0:
    result = result * 10 + num % 10
    num = num // 10
print(result)


# Version_2 - Ддля случаев, когда работа не с числами идет
# num = int(input('Введите целое число: '))
# result = ''
# for i in num:
#     result = i + result
# print(result)

# Version_3
# num = int(input('Введите целое число: '))
# result = num[::-1]
# print(result)


#=====================================================================================================================
# мой вариант

# num = input('Введите число для преобразования: ')
#
# list_numbers = []
# list_revers = []
#
# for i in num:
#     list_numbers.append(int(i))
#
# for i in reversed(list_numbers):
#     list_revers.append(i)
# print(''.join([str(i) for i in list_revers]))

