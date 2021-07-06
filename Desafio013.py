import emoji
print('=-='*10)
print('''\033[7m          DESAFIO 013           \033[m''')
print('=-='*10)
print(emoji.emojize(''':bulb: \033[1mFaça uma algoritmo que leia o salário de um funcionário e mostre seu novo salário, 
com 15% de aumento.\033[m''', use_aliases=True))
print('')
print('\033[7mREAJUSTE SALARIAL\033[m')
print('')
n1 = float(input('\033[1mDigite o salário:\033[m '))
n2 = int(input('\033[1mDigite quantos % teve de aumento:\033[m '))
print(f'\033[1mCom reajuste salarial em \033[m\033[1;35m{n2}%\033[m\033[1m seu salário '
      f'será \033[m\033[1;35mR${n1 * (n2 / 100) + n1:.2f}\033[m')

