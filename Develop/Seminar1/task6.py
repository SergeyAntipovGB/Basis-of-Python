'''
Задача 6: Вы пользуетесь общественным транспортом?
Вероятно, вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером,
где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
Вам требуется написать программу, которая проверяет счастливость билета.

*Пример:*

385916 -> yes
123456 -> no
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''


ticket = input("Введите шестизначный номер билета > ")
if len(ticket) != 6:
	print('Введено неверное значение')
else:
	left = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
	right = int(ticket[3]) + int(ticket[4]) + int(ticket[5])
	if left == right:
		print(f'{ticket} -> yes')
	else:
		print(f'{ticket} -> no')