profit = int(input('Введите доход: '))
if profit < 10000:
	tax = profit * 0.13
elif (profit >= 10000 and profit <= 50000):
	tax = (profit - 10000) * 0.2 + 10000 * 0.13
else:
	tax = (profit - 50000) * 0.3 + 40000 * 0.2 + 10000 * 0.13
print('Налог: ', tax)