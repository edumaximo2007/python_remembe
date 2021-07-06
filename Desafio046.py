import emoji
from time import sleep
from pygame import mixer
print('=-='*10)
print('''\033[7m         DESAFIO 046          \033[m''')
print('=-='*10)
print('')
print(emoji.emojize(''':bulb: \033[1mFaça um programa que mostre na tela uma\033[m\033[1;35m contagem regressiva\033[m\033[1m para o estouro de fogos de artifício, indo de \033[m\033[1;32m10 até 0\033[m\033[1m, com uma pausa de\033[m\033[1;35m 1 segundo\033[m\033[1m entre eles.\033[m''', use_aliases=True))
print('')
print('\033[7mCONTAREGEM REGRESSIVA\033[m')
print('')
cont = 0
for c in range(10, -1, -1):
    print(f'\033[1m{c}\033[m')
    sleep(1)
mixer.init()
mixer.music.load('fogos.mp3')
mixer.music.play()
cabum = str(input('.'))


