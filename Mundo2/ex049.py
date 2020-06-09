# Desafio 041

from datetime import date

print('-=-'*6,'Confederação Nacional de Natação','-=-'*6)
ano = int(input('Informe o ano de nascimento do atleta: '))

atual = date.today().year
idade = atual-ano

if idade < 9:
    print('O atleta é da categoria MIRIM.')
elif 9 <= idade < 14:
    print('O atleta é da categoria INFANTIL.')
elif 14 <= idade < 19:
    print('O atleta é da categoria JUNIOR.')
elif 19 <= idade < 20:
    print('O atleta é da categoria SÊNIOR.')
else:
    print('O atleta é da categoria MASTER.')
