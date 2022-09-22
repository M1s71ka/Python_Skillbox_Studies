number = int(input('Введите четырёхзначное число: '))
first = (number // 1000 % 10)
second = number // 100 % 10
third = number // 10 % 10
fourth = number % 10
print('Число: ', number, 'Число наоборот: ', fourth, third, second, first)