'''
Задача 30:
Заполните массив элементами арифметической прогрессии.
Её первый элемент, разность и количество элементов нужно ввести с
клавиатуры. Формула для получения n-го члена прогрессии:
an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
'''


def fun(count = 1):
    if count > n: return progressy
    progressy.append(a1 + (count - 1) * d)
    return fun(count + 1)

a1 = int(input('введи первый элемент прогрессии > '))
d = int(input('введи разность прогрессии > '))
n = int(input('введи количество элементов прогрессии > '))
progressy = list()
print(fun())