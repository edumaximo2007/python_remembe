import emoji
print('=-='*10)
print('''\033[7m          DESAFIO 006       \033[m''')
print('=-='*10)
print(emoji.emojize(''':bulb: \033[1mCrie um algoritmo que leia um número e mostre seu dobro, triplo e raiz quadrada.\033[m''', use_aliases=True))
print('')
print('\033[7mDOBRO, TRIPLO E RAIZ QUADRADA\033[m')
print('')
n = int(input('\033[1mDigite um número: '))
do = n * 2
t = n * 3
d = n ** (1 / 2)
print('\033[1mO \033[1;35mdobro\033[m\033[1m de\033[m\033[1;32m {}\033[m\033[1m e \033[m\033[1;35m{}\033[m\033[1m, seu \033[m\033[1;31mtriplo\033[m\033[1m e\033[m\033[1;31m {}\033[m\033[1m, e a sua \033[m\033[1;37mraiz quadrada\033[m\033[1m e \033[m\033[1;37m{:.1f}\033[m'.format(n, do, t, d))
