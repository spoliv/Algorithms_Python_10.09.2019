# 7. По длинам трех отрезков, введенных пользователем,
# определить возможность существования треугольника,
# составленного из этих отрезков. Если такой треугольник
# существует, то определить, является ли он разносторонним,
# равнобедренным или равносторонним.

a = int(input('Введите длину первого отрезка: '))
b = int(input('Введите длину второго отрезка: '))
c = int(input('Введите длину третьего отрезка: '))
if (a < (b + c)) & (b < (a + c)) & (c < (a + b)):
    if a == b & a == c:
        print('Треугольник существует и он равносторонний')

    elif (a != b) & (b != c) & (a != c):
        print('Треугольник существует и он разносторонний')
    else:
        print('Треугольник существует и он равнобедренный')
else:
    print('Треугольника не существует')