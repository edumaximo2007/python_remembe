import emoji

print('=-='*10)
print('''\033[7m         DESAFIO 056          \033[m''')
print('=-='*10)
print(emoji.emojize(''':bulb: \033[1mDesenvolva um programa que leia o \033[m\033[1;32mnome\033[m\033[1m, \033[m
\033[1;32midade\033[m\033[1m e \033[m\033[1;32msexo\033[m\033[1m de\033[m\033[1;35m 4 pessoas\033[m\033[1m.
No final do programa, mostre:\033[m

\033[1;32m:arrow_forward:\033[m\033[1m A\033[m\033[1;35m média de idade\033[m\033[1m do grupo.\033[m
\033[1;32m:arrow_forward:\033[m\033[1m Qual é o nome do homem \033[m\033[1;35mmais velho\033[m\033[1m.\033[m
\033[1;32m:arrow_forward:\033[m\033[1m Quantas mulheres têm\033[m\033[1;35m menos de 20\033[m\033[1m anos.\033[m''',
                    use_aliases=True))
print('')
print('\033[7mANALISADOR COMPLETO\033[m')
print('')
m = 0
v = ''
m20 = 0
me = 0
for p in range(1, 5):
    print(f'\33[1m{p}\033[m')
    n = str(input('\033[1mNome:\033[m ')).strip()
    i = int(input('\033[1mIdade:\033[m '))
    s = str(input('\033[1mSexo:\033[m '))[0]
    me = i / p
    if p == 1 and s in 'Mm':
        v = n
    if s in 'Mm' and i > m:
        m = i
        v = n
    if s in 'Ff' and i < 20:
        m20 = m20 + 1
print(f'\033[1mA média de idade do grupo e de {me}\033[m')
print(f'\033[1mO homem mais velho e o {v}\033[m')
print(f'\033[1mTem {m20} mulheres com menos de 20 anos\033[m')
