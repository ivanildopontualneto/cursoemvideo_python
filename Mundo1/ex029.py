#desafio026

frase = input('Digite uma frase: ').strip()
print('A letra "A" aparece {} vezes.'.format(frase.lower().count('a')))
print('A letra "A" aparece pela primeira vez na posição {}.'.format(frase.lower().find('a')+1))
print('A letra "A" aparece pela última vez na posição {}'.format(frase.lower().rfind('a')+1))
