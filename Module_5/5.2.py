x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
z = int(input('Введите третье число: '))
if x >= y and x >= z:
	print('Наибольшее число: ', x)
elif x >= y and x <= z:
	print('Наибольшее число: ', z)
elif x <= y and y >= z:
	print('Наибольшее число: ', y)
else:
	print('Наибольшее число: ', z)