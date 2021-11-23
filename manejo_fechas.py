from datetime import datetime, date

my_time = datetime.now()
print(my_time)

my_day = date.today()
print(my_day)

print(f'Year: {my_day.year}')
print(f'Month: {my_day.month}')
print(f'Day: {my_day.day}')

# Formateo de fechas

my_str =my_time.strftime('%d/%m/%Y')
print(f'Formato LATAM: {my_str}')

my_str =my_time.strftime('%m/%d/%Y')
print(f'Formato USA: {my_str}')

my_str =my_time.strftime('Estamos en el año %Y')
print(f'Formato Ramdon: {my_str}')