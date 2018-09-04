"""
7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между
собой (оба являться минимальными), так и различаться.
"""


# Не осилил


import random

SIZE = 20
array = [random.randint(-100, 100) for _ in range(SIZE)]
print(array)

#Version_1

# if array[0] > array[1]:
#     min_idx_1 = 0
#     min_idx_2 = 1
# else:
#     min_idx_1 = 1
#     min_idx_2 = 0
#
# for i in range(2, SIZE):
#     if array[i] < array[min_idx_1]:
#         tmp_idx = min_idx_1
#         min_idx_1 = i
#         if array[tmp_idx] < array[min_idx_2]:
#             min_idx_2 = tmp_idx
#
#     elif array[1] < array[min_idx_2]:
#         min_idx_2 = 1
#
# print(f'Число {array[min_idx_1]} в ячейке {min_idx_1}')
# print(f'Число {array[min_idx_2]} в ячейке {min_idx_2}')


#Version_1

min_1 = min(array)
array.remove(min_1)
min_2 = min(array)
print(min_1, min_2)




