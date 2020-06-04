#desafio017

from math import sqrt, pow, trunc, hypot

cateto_oposto = float(input('Informe o valor do cateto oposto: '))
cateto_adjacente = float(input('Informe o valor do cateto adjacente: '))
#hipotenusa = (pow(cateto_oposto, 2) + pow(cateto_adjacente, 2))
#print('O comprimento da hipotenusa vale {:.2f}.'.format(sqrt(hipotenusa)))

print('O comprimento da hipotenusa vale {:.2f}.'.format(hypot(cateto_oposto, cateto_adjacente)))
