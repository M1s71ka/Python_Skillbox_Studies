hours = int(input('Введите отработанные часы: '))
credit = int(input('Введите остаток по кредиту: '))
food = int(input('Введите траты на еду: '))
salary = 200 * hours / 8 + hours
if salary >= (credit + food):
	print('Часов хватает. Можно отдохнуть')
else:
	print('Часов не хватает. Придётся работать!')
	
