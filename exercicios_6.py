# Importe de função datetime

from datetime import datetime



# Solicitação da hora fornecida

hora = input("Forneça a hora desejada, neste formato (hh:mm):")

# conversão de string para hora

h_fornecida = datetime.strptime(hora,'%H:%M').time()

# verificação do da hora fornecida utilazando if, else.

if h_fornecida >= datetime.strptime('00:00','%H:%M').time() and h_fornecida <= datetime.strptime('11:59','%H:%M').time():
    print('Bom dia!!!')
elif h_fornecida >= datetime.strptime('12:00','%H:%M').time() and h_fornecida <= datetime.strptime('17:59','%H:%M').time():
    print('Boa tarde!!!')
else:
    print('Boa noite!!')