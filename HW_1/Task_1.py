"""
Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""

# Вариант из лекции

num = int(input('Введите трехзначное число: '))

a = num // 100
b = num % 100 // 10
c = num % 10

print(f' sum = { a + b + c }')
print(f' mult = { a * b * c }')

# Мой первоначальный вариант
# number = list(str(input('Введите трехзначное число: ')))
#
# one = int(number[0])
# two = int(number[1])
# three = int(number[2])
#
# print(one + two + three)
# print(one * two * three)
