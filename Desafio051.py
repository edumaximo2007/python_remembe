import emoji
print('=-='*10)
print('''\033[7m          DESAFIO 051         \033[m''')
print('=-='*10)
print(emoji.emojize(''':bulb: \033[1mDesenvolva um programa que leia o \033[m\033[1;35mprimeiro termo \033[m
\033[1me a\033[m\033[1;35m razão\033[m\033[1m de uma \033[m\033[1;32mPA\033[m\033[1m. No final, mostre os\033[m
\033[1;32m10\033[m\033[1m primeiros termos dessa progressão.\033[m''', use_aliases=True))
print('')
print('\033[7mPROGRESSÃO ARITMÉTICA\033[m')
print('')
soma = cont = 0
n1 = int(input('\033[1mDigite um número para fazer a \033[m\033[1;35mPA\033[m\033[1m:\033[m '))
n2 = int(input('\033[1mDigite a razão da PA:\033[m '))
decimo = n1 + (10 -1) * n2
for c in range(n1, decimo + n2, n2):
    print(f'\033[1m{c}\033[m', end=' ')
