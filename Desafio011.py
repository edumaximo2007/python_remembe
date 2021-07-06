import emoji
print('=-='*10)
print('''\033[7m          DESAFIO 011           \033[m''')
print('=-='*10)
print(emoji.emojize(''':bulb: \033[1mFaça um programa que leia a largura e a altura de uma parede em metros, calcule a 
sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
\033[m''', use_aliases=True))
print('')
print('\033[7mPINTANDO PAREDE\033[m')
print('')
n1 = float(input('\033[1mAltura da parede em mt:\033[m '))
n2 = float(input('\033[1mLargura da parede em mt:\033[m '))
print('')
print(f'\033[1mPara pintar uma parede de {n1 * n2:.1f}mt² e necessário {n1 * n2 / (2):.1f}l de tinta\033[m')
