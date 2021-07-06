import emoji
print('=-='*10)
print('''\033[7m          DESAFIO 008           \033[m''')
print('=-='*10)
print(emoji.emojize(''':bulb: \033[1mEscreva um programa que leia um valor em metros e o exiba convertido em centimetros e milímetros.\033[m''', use_aliases=True))
print('')
print('\033[7mCONVERSOR DE MEDIDAS\033[m')
print('')
n = float(input('\033[1mDigite um número em metros:\033[m '))
c = n * 100
m = n * 1000
print(f'\033[1m{n}Mt tem {c}Cm e {m}Mm\033[m')