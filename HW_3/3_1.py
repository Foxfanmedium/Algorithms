"""
1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.
"""

list_1 = [0]*8
print(list_1)

for i in range(2,100):
    for j in range(2,10):
        if i%j == 0:
            list_1[j-2] += 1

for i, item in enumerate(list_1, start=2):
    print(f'Числу {i} кратно {item} чисел')
