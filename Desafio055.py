import emoji
print('=-='*10)
print('''\033[7m         DESAFIO 055          \033[m''')
print('=-='*10)
print(emoji.emojize(''':bulb: \033[1mfaça um programa que leia o\033[m\033[1;32m peso\033[m\033[1m de \033[m
\033[1;35mcinco pessoas\033[m\033[1m. No final, mostre qual foi o\033[m\033[1;32m maior\033[m\033[1m e o \033[m
\033[1;32mmenor\033[m\033[1m peso lidos.\033[m''', use_aliases=True))
print('')
print('\033[7mMAIOR E MENOR SEQUÊNCIA\033[m')
print('')
pmaior = 0
pmenor = 0
for c in range(1, 6):
    n = float(input(f'\033[1mDigite o peso da {c}° pessoa:\033[m '))
    if c == 1:
        pmaior = n
        pmenor = n
    else:
        if n > pmaior:
            pmaior = n
        if n < pmenor:
            pmenor = n
print(f'\033[1mO maior peso lido e de {pmaior}Kg', end=' ')
print(f'\033[1mé o menor peso e de {pmenor}Kg\033[m')
