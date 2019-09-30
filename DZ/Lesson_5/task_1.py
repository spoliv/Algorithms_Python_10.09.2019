from collections import defaultdict, namedtuple

fabrics = defaultdict(list)
n = int(input('Введите количество предприятий:'))
sum_profit = 0

for i in range(n):
    name = input('Введите название: ')
    profit_year = float(input('Ведите прибыль за 1 квартал: ')) + \
              float(input('Ведите прибыль за 2 квартал: ')) + \
              float(input('Ведите прибыль за 3 квартал: ')) + \
              float(input('Ведите прибыль за 4 квартал: '))
    fabrics[i].append(name)
    fabrics[i].append(profit_year)
    sum_profit += profit_year
print(fabrics)
aver_profit = sum_profit / n
print(f'Среднегодовая прибыль {aver_profit: .2f}')
for i in range(n):
    if fabrics[i][1] > aver_profit:
        print(f'Прибыль {fabrics[i][0]} выше среднегодовой ')
    elif fabrics[i][1] < aver_profit:
        print(f'Прибыль {fabrics[i][0]} ниже среднегодовой ')
    else:
        print(f'Прибыль {fabrics[i][0]} равна среднегодовой ')


#Fabric = namedtuple('')
