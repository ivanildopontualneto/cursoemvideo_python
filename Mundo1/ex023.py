#desafio021

from pygame import mixer

mixer.init()
mixer.music.load('teste.mp3')
mixer.music.play()
input('Parar de tocar? (S) >')
