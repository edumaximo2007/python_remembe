import emoji
print('=-='*10)
print('''\033[7m          DESAFIO 003         \033[m''')
print('=-='*10)
print(emoji.emojize(''':bulb: \033[1;34mCrie um script Python que leia dois números e tente mostrar a soma entre eles.\033[m''',use_aliases=True))
print('')
print('\033[7mSOMANDO VALORES V1.0\033[m')
print('')
n1 = int(input('\033[1mDigite o 1° número:\033[m '))
n2 = int(input('\033[1mDigite o 2° número:\033[m '))
soma = n1 + n2
print(f'\033[1m{n1} + {n2} = \033[m\033[1;32m{soma}\033[m')
