# Desafio 038

n1 = int(input('Informe o primeiro valor: '))
n2 = int(input('Informe o segundo valor: '))

if n1 > n2:
    print('O primeiro valor ({}) é maior do que o segundo ({}).'.format(n1, n2))
elif n2 > n1:
    print('O segundo valor ({}) é maior do que o primeiro ({}).'.format(n2, n1))
else:
    print('Os dois valores são iguais.')
