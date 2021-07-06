import emoji
print('=-='*10)
print('''\033[7m          DESAFIO 009         \033[m''')
print('=-='*10)
print(emoji.emojize(''':bulb: \033[1mFaça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada.
\033[m''', use_aliases=True))
print('')
print('\033[7mTABUADA V1.0\033[m')
print('')
n = int(input('\033[1mDigite um número:\033[m '))

print('''{} x {:2} = {}
{} x {:2} = {}
{} x {:2} = {}
{} x {:2} = {}
{} x {:2} = {}
{} x {:2} = {}
{} x {:2} = {}
{} x {:2} = {}
{} x {:2} = {}
{} x {:2} = {}'''.format(n, 1, (n * 1), n, 2, (n * 2), n, 3, (n *3), n, 4, (n * 4), n, 5, (n * 5), n, 6, (n * 6), n, 7,
                         (n * 7), n, 8, (n * 8), n, 9, (n * 9), n, 10, (n * 10)))
