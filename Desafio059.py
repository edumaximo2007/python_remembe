import emoji
print('=-='*10)
print('''\033[7m         DESAFIO 059          \033[m''')
print('=-='*10)
print(emoji.emojize(''':bulb: \033[1mCrie um programa que leia\033[m\033[1;32m dois valores\033[m\033[1m e mostre um
\033[m\033[1;35mmenu\033[m\033[1m na tela:\033[m

\033[1;32m[1]\033[m\033[1;35m somar\033[m
\033[1;32m[2]\033[m\033[1;35m multiplicar\033[m
\033[1;32m[3]\033[m\033[1;35m maior\033[m
\033[1;32m[4]\033[m\033[1;35m novos números\033[m
\033[1;32m[5]\033[m\033[1;35m sair do programa\033[m

\033[1mSeu programa deverá realizar a operação solicitada em cada caso.\033[m''', use_aliases=True))
print('')
print('\033[7mCRIANDO MENU DE OPÇÕES\033[m')
print('')
n1 = int(input('\033[1mDigite o 1° número:\033[m '))
n2 = int(input('\033[1mDigite o 2² número:\033[m' ))
menu = soma = multiplicar = maior = 0
while menu != 5:
    menu = int(input('''\033[1m====SELECIONE====\033[m
    \033[1;32m[1]\033[m\033[1;35m SOMAR\033[m
    \033[1;32m[2]\033[m\033[1;35m MULTIPLICAR\033[m
    \033[1;32m[3]\033[m\033[1;35m MAIOR\033[m
    \033[1;32m[4]\033[m\033[1;35m NOVOS NÚMEROS\033[m
    \033[1;32m[5]\033[m\033[1;35m SAIR\033[m
    \033[1mopção: ''' ))
    if menu == 1:
        soma = n1 + n2
        print(f'\033[1m{n1} + {n2} = \033[m\033[1;35m{soma}\033[m')
    elif menu == 2:
        multiplicar = n1 * n2
        print(f'\033[1m{n1} x {n2} = \033[m\033[1;35m{multiplicar}\033[m')
    elif menu == 3:
        if n1 > n2:
            print(f'\033[1m{n1} e maior que {n2}\033[m')
        elif n2 > n1:
            print(f'\033[1m{n2} é maior que {n1}\033[m')
        else:
            print(f'\033[1m{n1} e {n2} são iguais\033[m')
    elif menu == 4:
            n1 = int(input('\033[1mDigite o 1° número:\033[m '))
            n2 = int(input('\033[1mDigite o 2° número:\033[m '))
    elif menu == 5:
        print('\033[1mFechando aplicação\033[m')
    else:
        print('\033[1;31mOpção inválida tente novamente\033[m')
