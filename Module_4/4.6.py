first_dice = int(input('Кубик Кости: '))
second_dice = int(input('Кубик владельца: '))
if first_dice >= second_dice:
	print('Разность: ', first_dice - second_dice)
	print('Костя платит')
else:
	print('Сумма: ', first_dice + second_dice)
	print('Владелец платит')
print('Игра окончена')
