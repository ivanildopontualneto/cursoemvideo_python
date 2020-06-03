#desafio006

n = int(input('Digite um número: '))
print('O dobro de {} vale {},\no triplo de {} vale {}\ne a raiz quadrada de {} é igual {:.2f}.'.format(n, (n*2), n, (n*3), n, (n**(1/2))))
#ou também pode ser pow(n,(1/2))