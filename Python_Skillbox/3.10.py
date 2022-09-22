a = int(input('Введите первое число: ')) # 3
b = int(input('Введите второе число: ')) # 5
print(a, b)
a += b # 8
b = abs(b - a)
a -= b
print(a, b)