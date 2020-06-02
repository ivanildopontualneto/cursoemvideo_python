#Primeiro desafio

# n1 = int(input('Digite o primeiro número: '))
# n2 = int(input('Digite o segundo número: '))
# s = n1 + n2
# print('A soma de {} e {} vale {}.'.format(n1, n2, s))

#Segundo desafio

#n = input('Digite algo: ')
#print('A variável é do tipo {}; Alfanumérica: {}; Numérica: {}; Alfabética: {}; Capitalizada: {}.'.format(type(n), n.isalnum(), n.isnumeric(), n.isalpha(), n.isupper()))

#Resolução

a = input('Digite algo: ')
print('O tipo primitivo desse valor é: {}.'.format(type(a)))
print('Só possui espaços? {}.'.format(a.isspace()))
print('É um número? {}.'.format(a.isnumeric()))
print('É alfabético? {}.'.format(a.isalpha()))
print('É alfanumérico? {}.'.format( a.isalnum()))
print('Está em maiúsculas? {}.'.format(a.isupper()))
print('Está em minúsculas? {}.'.format(a.islower()))
print('É capitalizada? {}.'.format(a.istitle()))
