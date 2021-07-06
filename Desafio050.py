import emoji
print('=-='*10)
print('''\033[7m          DESAFIO 050         \033[m''')
print('=-='*10)
print(emoji.emojize(''':bulb: \033[1mDesenvolva um programa que leia\033[m\033[1;35m seis números inteiros\033[m
\033[1m e mostre a soma apenas daqueles forem\033[m\033[1;32m pares\033[m\033[1m. Se o valor digitando for\033[m
\033[1;32m ímpar\033[m\033[1m, desconsidere-o.\033[m''', use_aliases=True))
print('')
print('\033[7mSOMA DOS PARES\033[m')
print('')
soma = cont = 0
for c in range(1, 7):
    n = int(input(f'\033[1mDigite o {c}° número\033[m: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print(f'\033[1mVocê digitou {cont} pares e a soma dos números e {soma}\033[m')

