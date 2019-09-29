import cProfile

# вариант с ситом


# def simple_by_num(n):
#     m = 10
#     while True:
#         sieve = [i for i in range(m)]
#         sieve[1] = 0
#         for i in range(2, m):
#             if sieve[i] != 0:
#                 j = i + i
#                 while j < m:
#                     sieve[j] = 0
#                     j += i
#         res = [i for i in sieve if i != 0]
#         if len(res) < n:
#             m += 1
#         else:
#             break
#     return res[n - 1]

# "task_2.simple_by_num(10)"
# 100 loops, best of 5: 170 usec per loop
# "task_2.simple_by_num(20)"
# 100 loops, best of 5: 991 usec per loop
# "task_2.simple_by_num(30)"
# 100 loops, best of 5: 2.52 msec per loop

# Сложность данного алгоритма O(n2). Это обусловлено двумя вложенными цикломи

# cProfile.run('simple_by_num(30)')
# 1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
# 105    0.000    0.000    0.000    0.000 {built-in method builtins.len}
# Похоже, встроенный метод exec-самое слабое звено


# вариант без сита

def simple_by_num(n):
    m = 10
    while True:
        arr_simple = []
        for i in range(2, m):
            if i in (2, 3, 5, 7) or i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
                arr_simple.append(i)
        if len(arr_simple) < n:
            m += 1
        else:
            break
    return arr_simple[n - 1]

# "task_2.simple_by_num(10)"
# 100 loops, best of 5: 104 usec per loop
# "task_2.simple_by_num(20)"
# 100 loops, best of 5: 709 usec per loop
# "task_2.simple_by_num(30)"
# 100 loops, best of 5: 2 msec per loop

#Сложность данного алгоритма также O(n2) по той же причине, но время
#выполнения немного меньше по причине меньшего количества обращений к массиву(1 раз
#вместо 2 в случае выше)

# cProfile.run('simple_by_num(30)')
# 1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
# 105    0.000    0.000    0.000    0.000 {built-in method builtins.len}
# 1808    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

#Встроенный метод exec-самое слабое звено
