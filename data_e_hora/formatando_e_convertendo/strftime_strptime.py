from datetime import datetime

data_atual = datetime.now()

# Formatação de data e hora
# print(data_atual.strftime("%d/%m/%Y %H:%M:%S"))
mask_pt_br = "%d/%m/%Y %H:%M:%S"
mask_pt_br_date = "%d/%m/%Y"
mask_us = "%m/%d/%Y %H:%M:%S"
print(data_atual.strftime(mask_pt_br))
print(data_atual.strftime(mask_pt_br_date))

date_string = "10/05/2020 12:46:31"

# Conversão de string para datetime
date = datetime.strptime(date_string, mask_us)
print(date)