#desafio035 -- Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

lado1 = float(input('Informe o primeiro comprimento de reta: '))
lado2 = float(input('Informe o segundo comprimento de reta: '))
lado3 = float(input('Informe o terceiro comprimento de reta: '))
if (lado1 + lado2 > lado3) and (lado2 + lado3 > lado1) and (lado1+lado3 > lado2):
    print('O triângulo pode existir.')
else:
    print('O triângulo não pode existir.')
