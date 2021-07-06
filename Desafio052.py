import emoji
print('=-='*10)
print('''\033[7m          DESAFIO 052         \033[m''')
print('=-='*10)
print(emoji.emojize(''':bulb: \033[1mFaça um programa que leia um\033[m\033[1;32m número inteiro\033[m\033[1m e diga se
ele é ou não um\033[m\033[1;35m número primo\033[m\033[1m.\033[m''', use_aliases=True))
print('')
print('\033[7mNÚMEROS PRIMOS\033[m')
print('')
total = 0
n = int(input('\033[1mDigite um número:\033[m '))
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[1;35m', end='')
        total += 1
    else:
        print('\033[1;33m', end='')
    print(f'\033[1m{c}\033[m', end=', ')
print(f'\033[1m o número \033[m\033[1;35m{n}\033[m\033[1m foi divisivel por {total}x\033[m')
if total == 2:
    print(f'\033[1mPortanto ele é um numero\033[m\033[1;35m PRIMO\033[m')
else:
    print('\033[1;31mEsse número não é primo\033[m')
