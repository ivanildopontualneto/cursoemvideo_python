# Aula 12

nome = input('Qual é o seu nome? ')
if nome == 'Ivanildo':
    print('Que nome bonito.')
elif nome == 'João' or nome == 'José' or nome == 'Maria' or nome == 'Pedro':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Luana':
    print('Que belo nome feminino.')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))
