""""
вывести наименование предприятия, чья прибыль вые среднего.
Отдельно вывести наименование предприятий, чья прибылт ниже реднего
"""

# Разбор урока
from collections import namedtuple

QUARTERS = 4

Company = namedtuple('Company', ['name', 'quarters', 'profit'])
all_companies = set()

num = int(input('Введите кол-во предприятий: '))

total_profit = 0

for i in range(1, num +1):
    profit = 0
    quarters = []
    name = input(f'Введите название предприятие {i}: ')

    for j in range(QUARTERS):
        quarters.append(int(input(f'Прибыль за  {j + 1}-й квартал: ')))
        profit += quarters[j]

    comp = Company(name=name, quarters = tuple(quarters), profit = profit)
    all_companies.add(comp)
    total_profit += profit

average = total_profit / num

print(f'\n Средняя прибыль = {average}')
print(f'\n Предприятия с прибылью выше среднего')

for comp in all_companies:
    if comp.profit > average:
        print(f'Компания {comp.name} заработала {comp.profit}')

print(f'\n Предприятие с прибылью ниже среднего: ')
for comp in all_companies:
    if comp.profit < average:
        print(f'Компания {comp.name} заработала {comp.profit}')








