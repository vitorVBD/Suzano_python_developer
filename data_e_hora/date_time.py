from datetime import date, datetime, time

#data e data atual
data = date(2020, 12, 31)
print(data)

data_atual = date.today()
print(data_atual)

#data e hora e data e hora atual
data_hora = datetime(2020, 12, 31, 23, 59, 59)
print(data_hora)

data_hora_atual = datetime.now()
print(data_hora_atual)

#hora e hora atual

hora = time(23, 59, 59)
print(hora)

hora_atual = datetime.now().time()
print(hora_atual)