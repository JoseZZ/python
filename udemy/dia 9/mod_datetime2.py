from datetime import datetime, date

fecha = datetime(2023, 10, 5, 12, 30, 45, 1000)
print(fecha)

fecha = fecha.replace(month=11)
print(fecha)

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
print(now.minute)

nacimiento = date(1990, 10, 5)
defuncion = date(2023, 6, 19)
vida = defuncion - nacimiento
print(vida)
print(vida.days)

despierta = datetime(2021, 10, 5, 7, 30, 45)
duerme = datetime(2021, 10, 5, 22, 40, 45)
vigilia = duerme - despierta
print(vigilia)
print(vigilia.seconds)