import os
from random import randint
os.system('clear')

'''
Задача 16: Требуется вычислить, сколько раз встречается некоторое
число X в массиве A[1..N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве. В последующих
строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    3
    -> 1
'''

n = int(input('введи натуральное число - количество элементов массива N = '))
a = [randint(0, 11) for i in range(n)]
print(a)
x = int(input('введи любое число (Х) из массива > '))
count = [i for i in a if i == x]
print(f'заданное число встречается в массиве {len(count)} раз(a)')