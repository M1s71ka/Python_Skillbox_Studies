hour = int(input('Введите время в часах: '))
if hour >= 8 and hour < 22 and (hour < 10 or hour >= 12 and hour != 14 and hour < 18 or hour >= 20):
	print('Можно получить поссылку')
else:
	print('Посылку получить нельзя')
	
