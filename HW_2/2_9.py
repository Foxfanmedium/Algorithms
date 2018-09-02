"""
9. Среди натуральных чисел, которые были введены,
найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
"""

# Version_1
num = int(input('Введите натуральное число. Ноль - выйти  '))
max_sum = 0
max_num = 0

while num != 0:
    temp_num = num
    temp_sum = 0
    while num > 0:
        temp_sum += num % 10
        num //= 10
    if temp_sum > max_sum
        max_sum = temp_sum
        max_num = temp_num
    num = int(input('Введите натуральное число. Ноль - выйти  '))
print(f'Число {max_num} имеет максимальную сумму цифр: {max_sum}')




# Version_2
# max_sum = 0
# max_num = 0
#
# while True:
#     num = input('Введите натуральное число. Ноль - выйти  ')
#     if num == '0':
#         break
#     temp_sum = sum(map(int, num))
#     if max_sum < temp_sum:
#         max_sum = temp_sum
#         max_num = int(num)
# print(f'Число {max_num} имеет максимальную сумму цифр: {max_sum}')


#=====================================================================================================================
# мой вариант

"""
Не решил
"""