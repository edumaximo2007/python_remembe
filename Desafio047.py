import emoji
print('=-='*10)
print('''\033[7m          DESAFIO 047         \033[m''')
print('=-='*10)
print(emoji.emojize(''':bulb: \033[1mCrie um programa que mostre na tela\033[m\033[1;35m todos os números pares\033[m
\033[1m que estão no intervalo entre\033[m\033[1;32m 1\033[m\033[1m e\033[m\033[1;32m 50\033[m\033[1m.\033[m
''', use_aliases=True))
print('')
print('\033[7mCONTAGEM DE PARES\033[m')
print('')
for n in range(2, 51, 2):
    print(f'\033[1m{n}\033[m', end=', ')
