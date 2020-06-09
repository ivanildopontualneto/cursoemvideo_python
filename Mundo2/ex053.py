# Desafio 045

from emoji import emojize
from random import randint

print('-=-'*8,emojize(':fist::hand::v:', use_aliases=True), 'Jokenpô', emojize(':fist::hand::v:', use_aliases=True), '-=-'*8,'\n')

opção = int(input('''\033[34mDigite \033[m1 \033[34mpara pedra.
Digite \033[m2 \033[34mpara papel.
Digite \033[m3 \033[34mpara tesoura\033[m.\n
Opção: '''))

cpu = (randint(1, 3))

if opção == 1 and cpu == 3:
    print('A MÁQUINA jogou: TESOURA!')
    print('Você \033[32mGANHOU!\033[m PEDRA amassa TESOURA!')
elif opção == 1 and cpu == 2:
    print('A MÁQUINA jogou: PAPEL!')
    print('Você \033[31mPERDEU!\033[m PAPEL embrulha PEDRA! :/')
elif opção == 2 and cpu == 1:
    print('A MÁQUINA jogou: PEDRA!')
    print('Você \033[32mGANHOU!\033[m PAPEL embrulha PEDRA!')
elif opção == 2 and cpu == 3:
    print('A MÁQUINA jogou: TESOURA!')
    print('Você \033[31mPERDEU!\033[m TESOURA corta PAPEL! :/')
elif opção == 3 and cpu == 2:
    print('A MÁQUINA jogou: PAPEL!')
    print('Você \033[32mGANHOU!\033[m TESOURA corta PAPEL!')
elif opção == 3 and cpu == 1:
    print('A MÁQUINA jogou: PEDRA!')
    print('Você \033[31mPERDEU!\033[m PEDRA amassa TESOURA! :/')
elif opção == cpu:
    print('A MÁQUINA jogou o mesmo que você!')
    print('\033[33mEMPATE!\033[m Tente novamente.')
else:
    print('ERRO! Opção inválida.')
