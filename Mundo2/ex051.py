# Desafio 043

altura = float(input('Informe sua altura: '))
peso = float(input('Informe sua peso: '))

imc = peso/(altura**2)

if imc < 18.5:
    print('Seu IMC é de {:.2f}. Você está ABAIXO DO PESO.'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu IMC é de {:.2f}. Você está no PESO IDEAL.'.format(imc))
elif 25 <= imc < 30:
    print('Seu IMC é de {:.2f}. Você está com SOBREPESO.'.format(imc))
elif 30 <= imc < 40:
    print('Seu IMC é de {:.2f}. Você está com OBESIDADE.'.format(imc))
else:
    print('Seu IMC é de {:.2f}. Você está com OBESIDADE MÓRBIDA!'.format(imc))
