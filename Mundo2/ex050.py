# Desafio 042

a = float(input('Informe o primeiro comprimento de reta: '))
b = float(input('Informe o segundo comprimento de reta: '))
c = float(input('Informe o terceiro comprimento de reta: '))

if a + b > c and a + c > b and b + c > a:
    print('É possível existir um triângulo.')
    if a == b == c:
        print('O triângulo é EQUILÁTERO!')
    elif a == b or a == c or b == c:
        print('O triângulo é ISÓSCELES!')
    else:
        print('O triângulo é ESCALENO!')
else:
    print('Não é possível existir um triângulo.')
