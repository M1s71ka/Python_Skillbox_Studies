mileage = int(input('Введите пробег: '))
number = int(input('Введите сегодняшнее число: '))
sum = 0
km = mileage
while (km > 0):
	sum += km % 10
	km = km // 10
if (sum > number):
	print('Сброс')
	mileage = 0;
else:
	print('Сегодня не сломался')
print('Пробег: ', mileage)