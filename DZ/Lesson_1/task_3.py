# 3. По введенным пользователем координатам двух
# # # точек вывести уравнение прямой вида y = kx + b,
# # # проходящей через эти точки.

x1 = int(input('Введите координату X первой точки: '))
y1 = int(input('Введите координату Y первой точки: '))
x2 = int(input('Введите координату X второй точки: '))
y2 = int(input('Введите координату Y второй точки: '))
k = (y2 - y1) / (x2 - x1)
b = y1 - k * x1
if b < 0:
    print(f'Через эти две точки проходит прямая вида y = {k: .2f} * x -{abs(b): .2f}')
else:
    print(f'Через эти две точки проходит прямая вида y = {k: .2f} * x + {b: .2f}')
