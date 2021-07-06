import emoji
print('=-='*10)
print('''\033[7m          DESAFIO 048        \033[m''')
print('=-='*10)
print('')
print(emoji.emojize(''':bulb: \033[1mFaça um programa que calcule a \033[m\033[1;32msoma\033[m\033[1m entre todos os \033[m\033[1;35mnúmeros ímpares\033[m\033[1m que são\033[m\033[1;32m múltiplos de três\033[m\033[1m e que se encontram no intervalo de \033[m\033[1;32m1\033[m\033[1m até\033[m\033[1;32m 500\033[m\033[1m.\033[m''', use_aliases=True))
print('')
print('\033[7mSOMA ÍMPARES MÚLTIPLOS DE TRÊS\033[m')
print('')
cont = 0
soma = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        soma += n
        cont = cont + 1
print(f'\033[1mA soma de todos os {cont} solicitado em igual à {soma}\033[m')
