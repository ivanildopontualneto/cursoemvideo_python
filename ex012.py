#desafio011
largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
print('A sua parede tem a dimensão de {}mx{}m com uma de área total {}m².'.format(largura, altura, area))
print('Para a sua parede serão necessários {}l (litros) de tinta.'.format(area/2))