#desafio018

from math import sin, cos, tan, radians

angulo = float(input('Informe um ângulo qualquer: '))
print('O seno de {}º é {:.2f}.\nO cosseno é {:.2f}. Por fim a tangente é {:.2f}.'.format(angulo, sin(radians(angulo)), cos(radians(angulo)), tan(radians(angulo))))

'''
from math import sqrt

angulo = int(input('Informe o ângulo desejado: '))
if angulo == 30:
    print('O seno do ângulo de {}º é {}.\nO cosseno é {:.3f} e a tangente é {:.3f}.'.format(angulo, (1/2), (sqrt(3)/2), (sqrt(3)/3)))
elif angulo == 45:
    print('O seno do ângulo de {}º é {:.3f}.\nO cosseno é {:.3f} e a tangente é {}.'.format(angulo, (sqrt(2)/2), (sqrt(2)/2), 1))
elif angulo == 60:
    print('O seno do ângulo de {}º é {:.3f}.\nO cosseno é {} e a tangente é {:.3f}.'.format(angulo, (sqrt(3)/2), (1/2), (sqrt(3))))
else:
    print('Indique um ângulo válido.')
'''