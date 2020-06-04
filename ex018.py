#desafio016

from math import trunc
num = float(input('Digite um número: '))
print('A porção inteira do valor real {} é {}.'.format(num, trunc(num)))

#ou {:.0f} ou int()