# Desafio 044

from time import sleep

preço = float(input('Informe o valor do produto: R$ '))
print('-=-'*6, 'Condições de Pagamento', '-=-'*6, '''\n
OPÇÃO (1): À Vista no Dinheiro - 10% de Desconto.
OPÇÃO (2): À Vista no Cartão de Crédito - 5% de Desconto.
OPÇÃO (3): Parcelado no Cartão de Crédito - Até 2x sem Juros.\n
Pressione 0 para sair.\n''')
print('-=-'*20, '\n')
opção = int(input('Informe a opção desejada: '))
print('Processando...')
sleep(2)
if opção == 1:
    print('O valor final a ser pago pelo produto será de R${:.2f}.'.format(preço-(preço*0.1)))
elif opção == 2:
    print('O valor final a ser pago pelo produto será de R${:.2f}.'.format(preço-(preço*0.05)))
elif opção == 3:
    parcelas = int(input('Qual o número total de parcelas? '))
    print('Processando...')
    sleep(2)
    if 0 < parcelas <= 2:
        print('O valor final a ser pago será de R${:.2f}.'.format(preço))
    elif parcelas > 2:
        print('O valor final a ser pago será de R${:.2f}.'.format(preço+(preço*0.2)))
    else:
        print('Erro: número inválido de parcelas! Fim da execução.')
else:
    print('Aplicação encerrada.')
