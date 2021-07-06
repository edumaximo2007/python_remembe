import emoji
print('=-='*10)
print('''\033[7m          DESAFIO 001         \033[m''')
print('=-='*10)
print(emoji.emojize(':bulb: \033[1mCrie um programa que escreva "Olá mundo" na tela\033[m', use_aliases=True))
print('')
print(emoji.emojize('\033[1mOlá mundo!!\033[m :earth_americas:', use_aliases=True))
