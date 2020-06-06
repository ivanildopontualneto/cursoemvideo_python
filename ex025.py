#desafio022

nome = input('Digite o seu nome completo: ')

print('Seu nome em maiúsculo: {}.'.format(nome.upper()))
print('Seu nome em minúsculo: {}.'.format(nome.lower()))
print('Seu nome completo possui ao todo {} letras.'.format(len(nome.replace(' ', ''))))
print('Seu primeiro nome possui {} letras.'.format(len(nome.split()[0])))
