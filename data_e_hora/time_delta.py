from datetime import timedelta, datetime, date, time

tipo_carro = "grande" # pequeno, medio, grande
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == "pequeno":
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f"O carro chegou às {data_atual} e ficará pronto às {data_estimada}")
elif tipo_carro == "medio":
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f"O carro chegou às {data_atual} e ficará pronto às {data_estimada}")
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f"O carro chegou às {data_atual} e ficará pronto às {data_estimada}")


print(date.today() - timedelta(days=1))

resultado = datetime(2020, 12, 15, 15, 45, 55) - timedelta(hours=1)
print(resultado.time())