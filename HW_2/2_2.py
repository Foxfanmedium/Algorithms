"""
Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560,
то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

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
