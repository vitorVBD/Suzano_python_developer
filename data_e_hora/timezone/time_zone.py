from datetime import datetime
import pytz

#criando datetime com timezone
current_date = datetime.now(pytz.timezone('America/Sao_Paulo'))
current_date_oslo = datetime.now(pytz.timezone('Europe/Oslo'))
print(current_date)
print(current_date_oslo)