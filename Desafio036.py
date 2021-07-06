import emoji
print('=-='*10)
print('''\033[7m         DESAFIO 036          \033[m''')
print('=-='*10)
print(emoji.emojize(''':bulb: \033[1mEscreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O
programa vai perguntar o \033[m\033[1;32mvalor da casa\033[m\033[1m, o \033[m\033[1;32msalário\033[m\033[1m do comprador
e em\033[m\033[1;32m quantos anos \033[m\033[1mele vai pagar.

\033[1;36mCalcule o valor da prestação mensal sabendo que ela não pode exceder\033[m\033[1;32m 30% \033[m\033[1;36m do
salário ou então o emprestimo será negado.\033[m''', use_aliases=True))
print('')
print('\033[7mAPROVANDO EMPRÉSTIMO\033[m')
print('')
imovel = float(input('\033[1mValor do imovel:\033[m '))
salario = float(input('\033[1mSalário do comprador\033[m '))
ano = int(input('\033[1mQuitar o emprestimo em quantos anos:\033[m '))
n = ano * 12
n1 = salario * (30 / 100)
n2 = imovel / ano
n3 = imovel / n
n4 = (imovel / n) - n1

if n4 < 0:
    print('=-='*10)
    print('\033[1;35mSeu emprestimo foi aprovado!!\033[m')
    print('=-='*10)
if n4 < 0:
    print(f'\33[1mValor do imovel R${imovel:.2f}, com parcelas de R${n3:.2f},\033[m'
          f'\033[1m durante {n} meses\033[m')
else:
    print(f'\033[1;31mEmprestimo negado\033[m\033[1m, você comprometeu \033[m'
          f'\033[1;31mR${n4:.2f}\033[m\033[1m da sua renda\033[m')






