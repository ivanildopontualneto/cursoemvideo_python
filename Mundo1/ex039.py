#desafio033 - ler três números e dizer qual é o maior e qual é o menor

n1 = float(input('Informe o primeiro número: '))
n2 = float(input('Informe o segundo número: '))
n3 = float(input('Informe o terceiro número: '))

# Menor número
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# Maior número
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O menor número é {}. O maior número é {}.'.format(menor, maior))
print('-=-'*6, 'Fim', '-=-'*6)

'''
if n1 > n2 > n3:
    print('{} é o maior número e {} é o menor.'.format(n1, n3))
if n1 > n3 > n2:
    print('{} é o maior número e {} é o menor.'.format(n1, n2))
if n2 > n1 > n3:
    print('{} é o maior número e {} é o menor.'.format(n2, n3))
if n2 > n3 > n1:
    print('{} é o maior número e {} é o menor.'.format(n2, n1))
if n3 > n1 > n2:
    print('{} é o maior número e {} é o menor.'.format(n3, n2))
if n3 > n2 > n1:
    print('{} é o maior número e {} é o menor.'.format(n3, n1))
if n1 == n2 and n1 > n3:
    print('{} (n1 e n2) é o maior número e {} é o menor.'.format(n1, n3))
if n1 == n2 and n1 < n3:
    print('{} é o maior número e {} (n1 e n2) é o menor.'.format(n3, n1))
if n1 == n3 and n1 > n2:
    print('{} (n1 e n3) é o maior número e {} é o menor.'.format(n1, n2))
if n1 == n3 and n1 < n2:
    print('{} é o maior número e {} (n1 e n3) é o menor.'.format(n2, n1))
if n2 == n3 and n2 > n1:
    print('{} (n2 e n3) é o maior número e {} é o menor.'.format(n2, n1))
if n2 == n3 and n2 < n1:
    print('{} é o maior número e {} (n2 e n3) é o menor.'.format(n1, n2))
if n1 == n2 == n3:
    print('Não há maior ou menor número.')
'''
