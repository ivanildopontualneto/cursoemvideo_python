n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}.'.format(m))
if m<7:
    print('Você foi reprovado.')
else:
    print('Você foi aprovado.')
