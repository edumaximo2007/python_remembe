import emoji
print('=-='*10)
print('''\033[7m          DESAFIO 044         \033[m''')
print('=-='*10)
print(emoji.emojize(''':bulb: \033[1mElabore um programa que calcule o valor a ser pago por um produto, considerando 
o seu\033[m\033[1;32m preço normal\033[m\033[1m e \033[m\033[1;32mcondição de pagamento\033[m\033[1m:\033[m

\033[1;32m-\033[m\033[1m À vista\033[m\033[1;35m dinheiro / cheque\033[m\033[1m: 
  \033[1;32m10%\033[m\033[1m de desconto\033[m
\033[1;32m-\033[m\033[1m À vista no \033[m\033[1;35mcartão\033[m\033[1m:\033[m
 \033[1;32m 5%\033[m\033[1m de desconto\033[m
\033[1;32m-\033[m\033[1m Em até\033[m\033[1;35m 2x no cartão\033[m\033[1m: preço normal\033[m
\033[1;32m-\033[m\033[1;35m 3x ou mais\033[m\033[1m no cartão:\033[m
 \033[1;32m 20%\033[m\033[1m de juros\033[m''', use_aliases=True))
print('')
print('\033[7mGERENCIADOR DE PAGAMENTOS\033[m')
print('')
n = float(input('\033[1mValor do produto:\033[m'))
print('')
n1 = int(input('''\033[1m===== OPÇÕES DE PAGAMENTO =====\033[m

\033[1;32m[1]\033[m\033[1m Dinheiro / Cheque 10% desconto.\033[m
\033[1;32m[2]\033[m\033[1m 1x no cartão 5% de deconsto.\033[m
\033[1;32m[3]\033[m\033[1m 2x sem juros no cartão.\033[m
\033[1;32m[4]\033[m\033[1m 3x no cartão com 20% de juros ou mais.\033[m

\033[1mSelecione a opção desejada\033[m: '''))
print('')
if n1 == 1:
    print(f'\033[1mR${n:.2f} com 10% de desconto dinheiro ou cheque pagando à vista R${n - (10 / 100) * n:.2f}\033[m')
elif n1 == 2:
    print(f'\033[1mR${n:.2f} com 5% de desconto 1x no cartão sem juros R${n - (5 / 100) * n:.2f}\033[m')
elif n1 == 3:
    print(f'\033[1mR${n:.2f} em 2x sem juros no cartão com parcelas de R${n / 2:.2f}\033[m')
elif n1 == 4:
    if n1 == 4:
        pa = int(input('\033[1mNúmero de parcelas:\033[m '))
        n3 = n / pa
        n4 = n3 * (20 / 100) + n3
        print(f'\033[1mR${n:.2f} em {pa}x no cartão com 20% de juros, com  parcelas de R${n4:.2f}\033[m')
else:
    print('\033[1;31mOpção inválida, tente novamente.\033[m')


