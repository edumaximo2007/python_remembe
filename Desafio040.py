import emoji
print('=-='*10)
print('''\033[7m          DESAFIO 040         \033[m''')
print('=-='*10)
print(emoji.emojize(''':bulb: \033[1mCrie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma 
mensagem no final, de acordo com a média antingida:\033[m

\033[1;32m-\033[m\033[1m Média abaixo de \033[m\033[1;32m5.0\033[m\033[1m:\033[m
\033[1;35mREPROVADO\033[m
\033[1;32m-\033[m\033[1m Média entre\033[m\033[1;32m 5.0\033[m\033[1m e \033[m\033[1;32m6.9\033[m\033[1m:\033[m
\033[1;35mRECUPERAÇÃO\033[m
\033[1;32m-\033[m\033[1m Média\033[m\033[1;32m 7.0\033[m\033[1m ou superior:\033[m
 \033[1;35mAPROVADO\033[m''', use_aliases=True))
print('')
print('\033[7mCLASSÍCO MÉDIA\033[m')
print('')
n1 = float(input('\033[1mDigite a 1° nota:\033[m '))
n2 = float(input('\033[1mDigite a 2° nota:\033[m '))
n = (n1 + n2) / 2
if n < 5:
    print(f'\033[1mVocê foi \033[m\033[1;31mREPROVADO\033[m\033[1m sua média foi {n}\033[m')
elif n <= 6.9:
    print(f'\033[1mVocê está em\033[m\033[1;32m RECUPERAÇÃO\033[m\033[1m sua média ficou {n}, muito abaixo do '
          f'\033[1mesperado estude mais\033[m')
elif n >= 7:
    print(f'\033[1mVocê foi\033[m\033[1;35m APROVADO\033[m\033[1m parabáns, sua média ficou {n}\033[m')
