"""
8. Посчитать, сколько раз встречается определенная цифра
в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать,
задаются вводом с клавиатуры.
"""

num = input('Введите последовательность чисел: ')
search_number = input('Введите цифру для подсчета: ')
counter = 0

list_of_figures = list(num)

for i in list_of_figures:
    if i == search_number:
        counter += 1

print(counter)