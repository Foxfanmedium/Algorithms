"""
8. Посчитать, сколько раз встречается определенная цифра
в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать,
задаются вводом с клавиатуры.
"""

#Version_1

num = int(input('Введите количество чисел: '))
digit = int(input('какую цийру посчитать: '))
count = 0
for i in range (1, num +1):
    m = int(input(f'Введите число {i}: '))
    while m > 0:
        if m % 10 == digit:
            count += 1
        m = m // 10

print(f'Было введено {count} цифр {digit}')

#Version_2
# num = int(input('Введите количество чисел: '))
# digit = int(input('какую цийру посчитать: '))
# count = 0
# for i in range (1, num +1):
#     ans = input(f'Введите число {i}: ')
#     count += ans.count(digit)
#
# print(f'Было введено {count} цифр {digit}')


#=====================================================================================================================
# мой вариант
# num = input('Введите последовательность чисел: ')
# search_number = input('Введите цифру для подсчета: ')
# counter = 0
#
# list_of_figures = list(num)
#
# for i in list_of_figures:
#     if i == search_number:
#         counter += 1
#
# print(counter)
