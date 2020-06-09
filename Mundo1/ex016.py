#desafio015

print('='*12, end='\n')
print('Aluguel de Carros')
print('='*12, end='\n')
dist = float(input("Qual o total de Km percorridos?"))
dias = int(input('Total de dias em que esteve alugado o veículo?'))

print('O preço total a pagar é de R${:.2f} reais.'.format((dias*60+dist*0.15)))