#Manipulando Textos

#Fatiamento

#frase = '   Curso em Vídeo Python  '
frase = 'Curso em Vídeo Python'
#print(frase[9:21:2])
#print(frase[:5])
#print(frase[15:])
#print(frase[9::3])
print(frase[::2])

#Análise

print(len(frase))
print(frase.count('o', 0, 13))
print(frase.find('deo')) #Posição
print(frase.find('Android')) #Não existe, -1
print('Curso' in frase) #True or False

#Transformação

print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())

#Divisão

print(frase.split())

#Junção

lista = ['Curso', 'em', 'Vídeo', 'Python']
print('_'.join(lista))

print('''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, 
sunt in culpa qui officia deserunt mollit anim id est laborum.\n''')

print(frase.upper().count('O'))
#print(len(frase.strip()))

frase = frase.replace('Python', 'Android')
print(frase)
print(frase.lower().find('android'))

dividido = frase.split()
print(dividido[0][3])
