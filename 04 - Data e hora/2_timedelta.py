from datetime import date, datetime, timedelta

size_car = "M"  # Pequeno, Médio, Grande
short_time = 30
middle_time = 45
large_time = 60
data_atual = datetime.now()

if size_car == "P":
    data_estimada = data_atual - timedelta(days=short_time)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
elif size_car == "M":
    data_estimada = data_atual - timedelta(days=middle_time)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
else:
    data_estimada = data_atual - timedelta(days=large_time)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")


print(date.today() - timedelta(days=1))

result_time = datetime(2023, 7, 25, 10, 19, 20) - timedelta(hours=1)
print(result_time.time())

print(datetime.now().date())
