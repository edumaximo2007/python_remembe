import emoji
print('=-='*10)
print('''\0337m       DESAFIO 057         \033[m''')
print('=-='*10)
print(emoji.emojize(''':bulb: \033[1mFaça um programa que leia o \033[m\033[1;32msexo\033[m\033[1m de uma pessoa, mas 
só aceite os valores \033[m\033[1;35m'M'\033[m\033[1m ou\033[m\033[1;35m 'F'\033[m\033[1m.
Caso esteja errado, peça a digitação novamente até ter um valor correto.\033[m''', use_aliases=True))
print('')
print('\033[7mVALIDAÇÃO DE DADOS\033[m')
print('')
c = ''
sexo = str(input('\033[1mSexo [M/F]:\033[m ')).strip().upper()[0]
while sexo not in 'MmFf':
    if sexo == 'Ff' in 'Mf':
        print('\033[1mDados correto\033[m')
    else:
        print('\033[1;31mOpção inválida, Preencha novamente\033[m')
    sexo = str(input('\033[1mSexo [M/F]:\033[m '))
