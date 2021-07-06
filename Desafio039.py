import emoji
from datetime import date
print('=-='*10)
print('''\033[7m          DESAFIO 039         \033[m''')
print('=-='*10)
print(emoji.emojize(''':bulb: \033[1mFaça um programa que leia o ano de nascimento de um jovem e informe, de acordo com
sua idade:

- Se ele\033[m\033[1;32m ainda vai se alistar\033[m\033[1m ao serviço militar.
- Se é a\033[m\033[1;32m hora de se alistar\033[m\033[1m.
- Se já\033[m\033[1;32m passou do tempo\033[m\033[1m do alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.''', use_aliases=True))
print('')
print('\033[7mALISTAMENTO MILITAR\033[m')
print('')
at = date.today().year
nas = int(input('\033[1mDigite o ano de nascimento:\033[m'))
ali = at - nas
if ali < 18:
    print(f'\033[1mVocê tem {ali} anos, falta {18 - ali} anos para você fazer o alistamento militar obrigatorio\033[m')
elif ali == 18:
    print(f'\033[1mChegou o momento para você fazer o alistamento militar obrigatorio, você completou {ali} anos\033[m')
elif ali > 18:
    print(f'\033[1mVocê tem {ali} anos e seu alistamento militar obrigatorio foi em {at - (ali - 18)}\033[m')

