#desafio012

preco = float(input('Digite o preço do produto: R$'))
print('O novo preço do produto de R${:.2f} reais, com 5% de desconto, é de R${:.2f} reais.'.format(preco, preco-(preco*0.05)))
