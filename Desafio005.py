import emoji
print('=-='*10)
print('''\033[7m          DESAFIO 005           \033[m''')
print('=-='*10)
print('')
print(emoji.emojize(''':bulb: \033[1mFaça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.\033[m''', use_aliases=True))
print('')
print('\033[7mANTECESSOR E SUCESSOR\033[m')
print('')
n = int(input('\033[1mDigite um número:\033[m '))
at = n - 1
sus = n + 1
print('\033[1mO \033[1;35mSUCESSOR\033[m\033[1m de\033[m\033[1;32m {}\033[m\033[1m e\033[m\033[1;35m {}\033[m\033[1m, é seu\033[m\033[1;31m ANTECESSOR\033[m\033[1m e \033[m\033[1;31m{}\033[m'.format(n, sus, at))
