# Desafio 040

n1 = float(input('Informe a primeira nota do aluno: '))
n2 = float(input('Informe a segunda nota do aluno: '))

media = (n1 + n2)/2

if media < 5.0:
    print('O aluno com a média {} está REPROVADO!'.format(media))
elif 5.0 <= media <= 6.9:
    print('O aluno com média {} está de RECUPERAÇÃO!'.format(media))
else:
    print('O aluno está APROVADO!')
