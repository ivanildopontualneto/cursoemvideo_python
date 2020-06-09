#desafio027

nome = input('Insira um nome completo: ')
print('Nome completo: {}.'.format(nome))
nome = nome.split()
print('Primeiro nome: {}.'.format(nome[0]))
#print(len(nome))
#print('Último nome: {}.'.format(nome[len(nome)-1]))
nome.reverse()
print('Último nome: {}.'.format(nome[0]))
