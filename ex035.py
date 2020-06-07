#desafio029

velocidade = float(input('Informe a velocidade em Km/h: '))
if velocidade > 80:
    excedente = (velocidade - 80)
    print('Você estava {}Km acima do limite permitido e será multado!\nSua multa será de R${:.2f} reais.'''.format(excedente, excedente*7))
else:
    print('Você estava a {}Km/h, logo, dentro do limite de velocidade.'.format(velocidade))
print('='*6,'Fim','='*6)
