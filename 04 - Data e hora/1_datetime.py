# or use the import such as: import datetime
from datetime import date, datetime, time

data = date(2023, 7, 10)
print(data)
print("Data de hoje:", date.today())


data_hora = datetime(2023, 7, 10)
print(data_hora)
print("Data e hora de hoje:", datetime.today())

hora = time(10, 20, 0)
print("Formatando horas:", hora)
