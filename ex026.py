#desafio023

num = int(input('Digite um número: '))
print('Unidade: {}.'.format((num//1%10)))
print('Dezena: {}.'.format(num//10%10))
print('Centena: {}.'.format(num//100%10))
print('Milhar: {}.'.format(num//1000%10))

'''
if(len(num) == 4):
    print('Unidade: {}.'.format(num[3]))
    print('Dezena: {}.'.format(num[2]))
    print('Centena: {}.'.format(num[1]))
    print('Milhar: {}.'.format(num[0]))
elif(len(num) == 3):
    print('Unidade: {}.'.format(num[2]))
    print('Dezena: {}.'.format(num[1]))
    print('Centena: {}.'.format(num[0]))
elif(len(num) == 2):
    print('Unidade: {}.'.format(num[1]))
    print('Dezena: {}.'.format(num[0]))
elif(len(num) == 1):
    print('Unidade: {}.'.format(num[0]))
else:
    print('Valor inválido.')
'''
