s = int(input('Введите площадь квартиры: '))
price = int(input('Введите стоимость квартиры: '))
if s >= 100 and price <= 10 or s >= 80 and price <= 7:
	print('Квартира подходит')
else:
	print('Квартира не подходит')