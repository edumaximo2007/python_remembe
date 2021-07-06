import emoji
from time import sleep
print('=-='*10)
print('''\033[7m          DESAFIO 049         \033[m''')
print('=-='*10)
print('')
print(emoji.emojize(''':bulb: \033[1mRefaça o\033[m\033[1;32m DESAFIO 009\033[m\033[1m, mostrando a \033[m
\033[1;35mtabuada\033[m\033[1m de um número que o usuário escolher, só que agora ultilizando um \033[m
\033[1;35mlaço for\033[m\033[1m.\033[m''', use_aliases=True))
print('')
print('\033[7mTABUADA V2.0\033[m')
print('')
cont = 0
mult = 0
n = int(input('\033[1mDigete um número para tabuada:\033[m '))
for c in range(1, 11):
    mult = n * c
    cont += 1
    print(f'\033[1m{n} x {c:2} = \033[m\033[1;31m{mult}\033[m')
    sleep(0.50)