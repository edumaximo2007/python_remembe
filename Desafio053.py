import emoji
print('=-='*10)
print('''\033[7m         DESAFIO 053          \033[m''')
print('=-='*10)
print(emoji.emojize(''':bulb: \033[1mCrie um programa que leia uma\033[m\033[1;32m frase\033[m\033[1m qualquer e diga 
se ela é um \033[m\033[1;35mpalíndromo\033[m\033[1m, desconsiderando os espaços.\033[m''', use_aliases=True))
print('')
print('\033[7mDETECTOR DE PAPLÍNDROMO\033[m')
print('')
f = str(input('\033[1mDigite uma frase:\033[m ')).strip().upper()
p = f.split()
j = ''.join(p)
i = ''
for l in range(len(j) - 1, - 1, - 1):
    i += j[l]
print(f'\033[1mO inverso de {f} é {i},\033[m', end=' ')
if i == j:
    print(f'\033[1m{i} é um \033[m\033[1;35mPALÍNDROMO\033[m')
else:
    print(f'\033[1m {f} não é um PALINDROMO\033[m')
