"""
Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""

number = list(str(input('Введите трехзначное число: ')))

one = int(number[0])
two = int(number[1])
three = int(number[2])

print(one + two + three)
print(one * two * three)
