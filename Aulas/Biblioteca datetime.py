import datetime

print(dir(datetime))
print(datetime.date.today())
print(datetime.datetime.now())

data = datetime.date(2022, 2, 23)
print(data)
print(data.year)
horario = datetime.datetime(2022, 2, 23, 8, 41, 0)
print(horario)
print(horario.minute)