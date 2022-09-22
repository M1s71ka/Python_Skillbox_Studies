a = int(input('Введите первое число: ')) 
b = int(input('Введите второе число: ')) 
print(a, b)
a += b 
b = abs(b - a)
a -= b
print(a, b)
