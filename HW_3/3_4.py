"""
4. Определить, какое число в массиве встречается чаще всего.
"""

# Мое решение
# Читерство или Python style, но пока своим умом не дошел как решить такую задачу
# import random
#
# lst = str([random.randint(50,80) for i in range(18)])
# search = lst.split()
# print(search)
# print(max(search, key=search.count))


# Version_1
import random

SIZE = 10
array = [random.randint(0, SIZE // 1.5) for _ in range(SIZE)]
print(array)

num = array[0]
max_frq = 1
for i in range(SIZE - 1):
    frq = 1
    for k in range(i +1, SIZE):
        if array[i] == array[k]:
            frq += 1
    if frq > max_frq:
        num = array[1]

if max_frq > 1:
    print(f'Число {num} встречается {max_frq} раз')
else:
    print('Все числа уникальны')
#----------------------------------------------------------------------------------
# Version_2
diction = {}
for item in array:
    if item in diction:
        diction[item] +=1
    else:
        diction[item] = 1

print(diction)


