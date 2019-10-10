# 3 Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите
# в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: в одной
# находятся элементы, которые не меньше медианы, в другой — не больше медианы.
#
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также
# недопустима).

import random


def median_square(array):
    for i in range(len(array)):
        smaller = equal = bigger = 0
        for j in range(len(array)):
            if array[i] < array[j]:
                smaller += 1
            elif array[i] > array[j]:
                bigger += 1
            else:
                equal += 1
        equal -= 1

        if smaller == bigger or smaller == equal + bigger or smaller + equal == bigger:
            return array[i]


m = int(input('Введите натуральное число: '))
LIMIT = 100
data = [random.randrange(0, LIMIT) for _ in range(2 * m + 1)]
print(data)
print(sorted(data))
print(f'Медиана в данном массиве = {median_square(data)}')
