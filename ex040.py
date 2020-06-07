#desafio034

salario = float(input('Informe o salário do funcionário que deve receber o aumento: '))
if salario <= 1250:
    print('Com o aumento de 15%, o salário de R${:.2f} reais passará a ser de R${:.2f} reais.'.format(salario, (salario+salario*0.15)))
else:
    print('Com o aumento de 10%, o salário de R${:.2f} reais passará a ser de R${:.2f} reais.'.format(salario, (salario+salario*0.1)))
print('='*6,'Fim','='*6)
