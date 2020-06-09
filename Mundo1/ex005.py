n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1+n2
d = n1/n2
m = n1*n2
di = n1//n2
e = n1**n2
print('A soma vale {}, \na divisão vale {:.3f} \ne o produto vale {}.'.format(s, d, m), end=' >>> ')
print('Divisão inteira {} e potência {}.'.format(di, e))
