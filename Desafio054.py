import emoji
from datetime import date
print('=-='*10)
print('''\033[7m         DESAFIO 054           \033[m''')
print('=-='*10)
print(emoji.emojize(''':bulb: \033[1mCrie um programa que leia o \033[m\033[1;32mano de nascimento\033[m\033[1m de\033[m
\033[1;35msete pessoas\033[m\033[1m. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas 
já são maiores.\033[m''', use_aliases=True))
print('')
print('\033[7mGRUPO MAIOR E MENOR IDADE\033[m')
print('')
menor = 0
maior = 0
at = date.today().year
for c in range(1, 8):
    print(f'{c}°')
    i = int(input('\033[1mAno de nascimento:\033[m '))
    a = at - i
    print('')
    if a < 21:
        menor += 1
    elif a >= 21:
        maior += 1
print(f'\033[1mExite {maior} maior de idade, é {menor} menor de idade\033[m')
