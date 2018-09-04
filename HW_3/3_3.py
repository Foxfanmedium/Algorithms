"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random
#
# SIZE = random.randint(5, 15)
# lst = [random.randint(-100, 100) for _ in range(SIZE)]
# print(lst)
# min_ = 0
# max_ = 0
# for i in range(len(lst)):
#     if lst[i] < lst[min_]:
#         min_ = i
#     elif lst[i] > lst[max_]:
#         max_ = i
# print(min_)
# print(max_)


# Решение с урока

SIZE = 10
array = [random.randint(-100, 100) for _ in range(SIZE)]
print(array)

# Version_1
idx_min = 0
idx_max = 0
#
# for i in range(len(array)):
#     if array[i] < array[idx_min]:
#         idx_min = i
#     elif array[i] > array[idx_max]:
#         idx_max = i
# print(f'Min = {array[idx_min]} в ячейке {idx_min}; Max = {array[idx_max]} в ячейке {idx_min}')
#
# spam = array[idx_min]
# array[idx_min] = array[idx_max]
# array[idx_max] = spam
# print(array)




# Version_2

min_num = min(array)
max_num = max(array)
idx_min = array.index(min_num)
idx_max = array.index(max_num)
print(f'Min = {array[idx_min]} в ячейке {idx_min}; Max = {array[idx_max]} в ячейке {idx_min}')
array[idx_min], array[idx_max] = array[idx_max], array[idx_min]
print(array)






