first = int(input('Введите стоимость первого товара: '))
second = int(input('Введите стоимость второго товара: '))
third = int(input('Введите стоимость третьего товара: '))
sum = first + second + third
if sum > 10000:
	sum *= 0.9
print(sum)
