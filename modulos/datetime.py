# https://docs.python.org/2/library/datetime.html
from datetime import datetime, timedelta
from locale import setlocale, LC_ALL

setlocale(LC_ALL, 'pt_BR.utf-8')
dataAtual = datetime.now()
formatacao = dataAtual.strftime('%A, %d de %B de %Y')
print(formatacao)

# Ano, mês, dia, hora, minuto, segundo(hora, minuto e segundo é opcional)
data = datetime(2019, 4, 20, 20, 53, 20)
# print(data.strftime('%d/%m/%Y'))


# strptime(str, fmt) -> vai criar um objeto de data a partir de uma string
# .strftime(fmt)
# timestamp
# fromtimestamp()


data = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
data = data + timedelta(seconds=2*60*60)
print(data.strftime('%d/%m/%Y %H:%M:%S'))