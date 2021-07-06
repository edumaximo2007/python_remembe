import emoji
print('=-='*10)
print('''\033[7m          DESAFIO           \033[m''')
print('=-='*10)
print('')
print(emoji.emojize(''':bulb: \033[1mFaça um algoritmo que leia o preço
de um prdoduto e mostre seu novo preço, com 5% de desconto.\033[m''', use_aliases=True))
print('')
print('\033[7mCALCULANDO DESCONTOS\033[m')
print('')
n1 = float(input('\033[1mValor do produto:\033[m '))
print(f'\033[1mO valor a ser pago com\033[m\033[1;35m 5%\033[m\033[1m de '
      f'desconto\033[m\033[1;35m R${n1 - (5 / 100) * n1:.2f}\033[m')
