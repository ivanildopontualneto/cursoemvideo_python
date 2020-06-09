#desafio028

from random import randint
from time import sleep

numero = randint(0, 5)
palpite = int(input('Em qual número eu estou pensando? (Entre 0 e 5) '))
print('Processando...')
sleep(2)
if numero == palpite:
    print('Parabéns, você é um verdadeiro professor Xavier!')
else:
    print('"Ai que burro, dá zero pra ele!"\nEu tava pensando no {}.'.format(numero))
print('='*6,'Fim','='*6)
