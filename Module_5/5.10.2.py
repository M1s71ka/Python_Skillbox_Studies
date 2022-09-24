hour = int(input('Введите время в часах: '))
if hour < 8 or hour >= 22 or hour >= 10 and hour < 12 or hour == 14 or hour >= 18 and hour < 20:
	print('Посылку получить нельзя')
else:
	print('Можно получить поссылку')