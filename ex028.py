#desafio025

nome = input('Insira seu nome: ')
print('Seu nome é {}.'.format(nome))
if 'silva' in nome.lower().split():
    print('Seu nome possui a palavra "Silva".')
else:
    print('Seu nome não possui a palavra "Silva".')
