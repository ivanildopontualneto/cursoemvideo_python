# Desafio 037

numero = int(input('Informe um número inteiro a ser convertido: '))
opção = int(input('''Para qual base deseja converter esse número?
OPÇÃO (1): Converter para Binário.
OPÇÃO (2): Converter para Octal.
OPÇÃO (3): converter para Hexadecimal.
Pressione 0 para sair.\n
Digite sua opção: '''))

if opção == 1:
    print('O número inteiro {} convertido em binário corresponde a {}.'.format(numero, bin(numero)))
elif opção == 2:
    print('O número inteiro {} convertido em octal corresponde a {}.'.format(numero, oct(numero)))
elif opção == 3:
    print('O número inteiro {} convertido em hexadecimal corresponde a {}.'.format(numero, hex(numero)))
else:
    print('Aplicação encerrada.')
