x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
z = int(input('Введите третье число: '))
if x >= y:
	max = x
else:
	max = y
if z > max:
	max = z
print(max)
