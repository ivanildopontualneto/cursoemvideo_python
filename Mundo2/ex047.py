# Desafio 039

from datetime import date

ano = int(input('Informe aqui o ano do seu nascimento: '))
data = date.today().year
idade = (data-ano)

if idade < 18:
    print('Você ainda vai se alistar no exército. Faltam {} anos para o seu alistamento.'.format(18-idade))
elif idade > 18:
    print('Já passou o período do seu alistamento. Isso foi há {} anos.'.format(idade-18))
else:
    print('Você está dentro do período de alistamento. Dirija-se à junta militar mais próxima.')
