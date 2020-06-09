# Desafio 036

from math import

casa = float(input('Qual o valor da casa a ser adquirida? '))
salario = float(input('Qual é o salário do comprador? '))
anos = int(input('Em quantos anos deve ser pago? '))

mensal = casa/(anos*12)

if mensal > (salario*0.3):
    print('Empréstimo negado: a prestação de R${:.2f} a ser paga em {} meses,\nexcede o valor de 30% do salário.'.format(mensal, (anos*12)))
else:
    print('Seu empréstimo foi aprovado com a mensalidade no valor de R${:.2f}.'.format(mensal))
