# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и
# позицию в массиве. Примечание к задаче: пожалуйста не путайте «минимальный» и
# «максимальный отрицательный». Это два абсолютно разных значения.

import random


SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

dict_ = {}
for i, elem in enumerate(array):
    if elem < 0:
        dict_[i] = abs(elem)
max_ = MAX_ITEM
key = 0
for i, elem in dict_.items():
    if elem < max_:
        max_ = elem
        key = i
print(f'Максимальный отрицательный элемент -{max_} и его позиция в массиве {key}')
