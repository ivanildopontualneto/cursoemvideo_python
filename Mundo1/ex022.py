#desafio020

from random import sample

aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
print('A ordem de apresentação dos trabalhos será: {}.'.format(sample(lista, k=len(lista))))


'''
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print('A ordem de apresentação dos trabalhos será:')
print(lista)
'''