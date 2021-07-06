import emoji
print('=-='*10)
print('''\033[7m          DESAFIO 007           \033[m''')
print('=-='*10)
print(emoji.emojize(''':bulb: \033[1mDesenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.\033[m''', use_aliases=True))
print('')
print('\033[7mMÉDIA ARITMEETICA\033[m')
print('')
nome = str(input('\033[1mNome: '))
n1 = float(input('\033[1mDigite a 1° nota: '))
n2 = float(input('\033[1mDigite a 2° nota: '))
me = (n1 + n2) / 2
print(f'\033[1m{nome} tirou {n1} na primeira nota e {n2} na segunda nota, sua média e {me}\033[m')
