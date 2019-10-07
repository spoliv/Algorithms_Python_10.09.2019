import sys
import random


def show_size(*args):
    size = 0
    sum_size = 0
    for arg in args:
        size = sys.getsizeof(arg)
        sum_size += size
        if hasattr(arg, '__iter__'):
            if hasattr(arg, 'items'):
                for key, value in arg.items():
                    size = sys.getsizeof(key) + sys.getsizeof(value)
                    sum_size += size
            elif not isinstance(arg, str):
                for item in arg:
                    size = sys.getsizeof(item)
                    sum_size += size
    print(f'Cуммарный объем памяти, занимаемый переменными {sum_size}')


# Найти сумму и произведение цифр трехзначного числа,
# которое вводит пользователь.

num = int(input('Введите трехзначное число: '))
a = (num - num % 100) / 100
b = (num % 100 - (num % 100) % 10) / 10
c = (num % 100) % 10
sum = a + b + c
prod = a * b * c
print(f'Сумма цифр = {sum}, произведение цифр = {prod}')

show_size(num, a, b, c, sum, prod)


# Пользователь вводит номер буквы в алфавите.
# Определить, какая это буква.

n = int(input('Введите номер буквы в алфавите: '))
n = ord('a') + n - 1
let = chr(n)
print(f'Это буква {let}')

show_size(n, let)


# Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан
# массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5,
# (индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array_1)

array_2 = []
for i, elem in enumerate(array_1):
    if elem % 2 == 0:
        array_2.append(i)
print(array_2)

show_size(SIZE, MIN_ITEM, MAX_ITEM, array_1, array_2, i, elem)

