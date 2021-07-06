import emoji
print('=-='*10)
print('''\033[7m          DESAFIO 038         \033[m''')
print('=-='*10)
print(emoji.emojize(''':bulb: \033[1mEscreva um programa que leia\033[m\033[1;35m dois números\033[m\033[1m inteiros e 
comparar-os monstrando na tela uma mensagem:\033[m

\033[1;32m-\033[m\033[1m O\033[m\033[1;32m primeiro valor\033[m\033[1m é \033[m\033[1;35mmaior\033[m
\033[1;32m-\033[m\033[1m O\033[m\033[1;32m segundo valor\033[m\033[1m é \033[m\033[1;35mmaior\033[m
\033[1;32m- Não existe\033[m\033[1m valor maior, os dois são\033[m\033[1;35m iguais\033[m''', use_aliases=True))
print('')
print('\033[7mCOMPARANDO NÚMEROS\033[m')
print('')
n1 = int(input('\033[1mDigite o 1° número:\033[m '))
n2 = int(input('\033[1mDigite o 2° número:\033[m '))

if n1 > n2:
    print(f'\033[1m{n1} e maior que {n2}\033[m')
elif n2 > n1:
    print(f'\033[1m{n2} e maior que {n1}\033[m')
elif n1 == n2:
    print(f'\033[1m{n1} não e maior nem menor {n2}\033[m')
