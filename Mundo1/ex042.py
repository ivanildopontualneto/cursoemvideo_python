#Exemplo ANSI Sequence

nome = 'Ivanildo'
print('\033[35mOlá Mundo!\033[m')
print('Olá e muito prazer, {}{}{}!'.format('\033[32m', nome, '\033[m'))
print('Olá e muito prazer, {}{}{}!'.format('\033[1;30;41m', nome, '\033[m'))