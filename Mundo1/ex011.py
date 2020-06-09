#desafio010

dinheiro = float(input('Quanto dinheiro você tem na carteira? R$'))
print('Com R${:.2f} reais você pode comprar US${:.2f} dólares.'.format(dinheiro, (dinheiro/5.20)))
print('Com R${:.2f} reais você pode comprar €{:.2f} euros.'.format(dinheiro, (dinheiro/5.83)))
print('Com R${:.2f} reais você pode comprar ¥{:.2f} ienes.'.format(dinheiro, (dinheiro/0.048)))
