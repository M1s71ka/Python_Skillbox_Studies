number = int(input('Введите четырёхзначное число: '))
second = number // 100
third = number // 10
print(number, ' состоит из цифр ', number // 1000, ',', second % 10, ',', third % 10, ',', number % 10)