minutes = int(input('Введите кол-во минут: '))
hours = minutes // 60
minutes_left = minutes % 60
print(minutes, ' - это ', hours, ' часов и ', minutes_left, ' минут.')