import emoji
print('=-=' * 10)
print('''\033[7m          DESAFIO 064         \033[m''')
print('=-=' * 10)
print(emoji.emojize(''':bulb: \033[1mCrie um programa que leia\033[m\033[1m vários números\033[m\033[1m inteiros pelo
teclado. O programa só vai parar quando o usuário digirar o valor\033[m\033[1;32m 999\033[m\033[1m, que é a\033[m
\033[1;35mcondição de parada\033[m\033[1m. No final, mostre\033[m\033[1;35m quantos números\033[m\033[1m foram digitados
e qual foi a \033[m\033[1;35msoma\033[m\033[1m entre eles\033[m\033[1;37m (descosiderando o flag)\033[m\033[1m.\033[m'''
                     , use_aliases=True))
