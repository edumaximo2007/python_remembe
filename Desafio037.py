import emoji
from time import sleep
print('=-'*10)
print('''\033[7m          DESAFIO 037           \033[m''')
print(emoji.emojize(''':bulb: \033[1mEscreva um programa que leia um número inteiro qualquer e peça para o usuário
escolher qual será a \033[m\033[1;35mbase de conversão\033[m\033[1m:\033[m

\033[1;32m-\033[m\033[1;35m1\033[m\033[1m para\033[m\033[1;32m binário\033[m
\033[1;32m-\033[m\033[1;35m2\033[m\033[1m para\033[m\033[1;32m octal\033[m
\033[1;32m-\033[m\033[1;35m3\033[m\033[1m para\033[m\033[1;32m hexadecimal\033[m''', use_aliases=True))
print('')
print('\033[7mCONVERSOR DE BASES NÚMERICAS\033[m')
print('')
n = int(input('\033[1mDigite um número inteiro:\033[m '))
op = int(input('''\033[1m[\033[m\033[1;32m1\033[m\033[1m] BINÁRIO
[\033[m\033[1;32m2\033[m\033[1m] OCTAL
[\033[m\033[1;32m3\033[m\033[1m] HEXADECIMAL
Escolha uma opção:\033[m '''))
sleep(0.50)
if op == 1:
    print(f'\033[1mO número {n} na sua versão binária e \033[m\033[1;35m{bin(n)[2:]}\033[m')
elif op == 2:
    print(f'\033[1mO número {n} na sua versão octal e \033[m\033[1;35m{oct(n)[2:]}\033[m')
elif op == 3:
    print(f'\033[1mO número {n} na sua versão hexadecimal e \033[m\033[1;35m{hex(n)[2:]}\033[m')
else:
    print('\033[1mOpção inválida\033[m')
