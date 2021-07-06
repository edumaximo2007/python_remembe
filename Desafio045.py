import emoji
from random import randint
print('=-='*10)
print('''\033[7m          DESAFIO 045         \033[m''')
print('=-='*10)
print(emoji.emojize(''':bulb: \033[1mCrie um programa que faça o computador jogar\033[m\033[1;32m Joenpô\033[m\033[1m com você.\033[m''', use_aliases=True))
print('')
print('\033[7mJOkENPÔ\033[m')
print('')
pc = randint(0, 2)
p1 = (':fist:', ':hand:', ':v:')
j = int(input(emoji.emojize('''\033[1mVamos jogar jokenpô\033[m
\033[1;32m[\033[m\033[1m0\033[m\033[1;32m]\033[m :fist:
\033[1;32m[\033[m\033[1m1\033[m\033[1;32m]\033[m :hand:
\033[1;32m[\033[m\033[1m2\033[m\033[1;32m]\033[m :v:

\033[1mSelecione a opção desejada:\033[m ''', use_aliases=True)))
print('')
print(emoji.emojize(':hand: :fist: :v: '*3, use_aliases=True))
print(emoji.emojize(f'''\033[1mComputador jogou \033[m\033[31m{p1[pc]}\033[m
\033[1mPlayer jogou \033[m\033[35m{p1[j]}\033[m''', use_aliases=True))
print(emoji.emojize(':hand: :fist: :v: '*3, use_aliases=True))
print('')
if pc == 0: #PEDRA
    if j == 0:
        print('\033[1mEmpate\033[m')
    elif j == 1:
        print('\033[1mPapel ganha de pedra, jogador venceu\033[m')
    elif j == 2:
        print('\033[1mPedra ganha de tesoura, \033[m\033[1;31mcomputador venceu\033[m')
elif pc == 1: #PAPEL
    if j == 1:
        print('\033[1mEmpate\033[m')
    elif j == 0:
        print('\033[1mPapel ganha de pedra, \033[m\033[1;31mcomputador venceu\033[m')
    elif j == 2:
        print('\033[1mTesoura ganha de papel, jogador venceu\033[m')
elif pc == 2: #TESOURA
    if j == 2:
        print('\033[1mEmpate\033[m')
    elif j == 0:
        print('\033[1mPedra ganha de tesoura, jogador venceu\033[m')
    elif j == 1:
        print('\033[1mTesoura ganha de papel, \033[m\033[1;31mcomputador venceu\033[m')
