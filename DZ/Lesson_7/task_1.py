# 1 Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный
# случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный
# массивы.
# Примечания:
# ● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# ● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка
# пузырьком. Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт
# не идут.


import random


def bubble_sort(array):
    n = 1

    while n < len(array):
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1


SIZE = 15
LIMIT = 100
data = [random.randrange(-LIMIT, LIMIT) for _ in range(SIZE)]
print(data)
bubble_sort(data)
print(data)