#desafio031

dist = float(input('Informe a distância total da viagem em Km: '))
if dist <= 200:
    print('A distância total da viagem é de {}Km.\nO preço da passagem será de R${:.2f} reais.'.format(dist, dist*0.5))
else:
    print('A distância total da viagem é de {}Km.\nO preço da passagem será de R${:.2f} reais.'.format(dist, dist*0.45))
print('='*6,'Fim','='*6)
