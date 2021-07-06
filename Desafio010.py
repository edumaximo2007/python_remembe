import emoji
print('=-='*10)
print('''\033[7m          DESAFIO 010           \033[m''')
print('=-='*10)
print('')
print(emoji.emojize(''':bulb: \033[1mCrie um programa que leia quanto dinheiro uma pessoa tem n carteira e mostre 
quantos dólares ela pode comprar.\033[m''', use_aliases=True))
print('')
print('\033[7mCONVERSOR DE MOEDAS\033[m')
print('')
n1 = float(input('\033[1mDigite o valor em R$:\033[m '))
n2 = float(input('\033[1mDólar USD$:\033[m '))
print(f'\033[1mCom R${n1:.2f} e possivel comprar USD${(n1 / n2):.2f}\033[m')
