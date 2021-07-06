import emoji
from datetime import date
print('=-='*10)
print('''\033[7m          DESAFIO 041         \033[m''')
print('=-='*10)
print('')
print(emoji.emojize(''':bulb: \033[1mA Confederação Nacional de natação precisa de um programa que leia o ano de 
nascimento de uma atleta e mostre a sua categoria, de acordo com a idade:\033[m

\033[1;32m-\033[m\033[1m Até\033[m\033[1;32m 9 anos \033[m\033[1m:\033[m\033[1;35m MIRIM\033[m
\033[1;32m-\033[m\033[1m Até\033[m\033[1;32m 14 anos\033[m\033[1m:\033[m\033[1;35m INFANTIL\033[m
\033[1;32m-\033[m\033[1m Até\033[m\033[1;32m 19 anos\033[m\033[1m:\033[m\033[1;35m JUNIOR\033[m
\033[1;32m-\033[m\033[1m Até\033[m\033[1;32m 20 anos\033[m\033[1m:\033[m\033[1;35m SÊNIOR\033[m
\033[1;32m-\033[m\033[1m Acima:\033[m\033[1;35m MASTER\033[m''', use_aliases=True))
print('')
print('\033[7mCLASSIFICANDO ATLETAS\033[m')
print('')
at = date.today().year
nas = int(input('\033[1mDigite o ano de nascimento:\033[m'))
n = at - nas
if n <= 9:
    print(f'\033[1mVocê tem {n} anos sua categoria e a \033[m\033[1;35mMIRIM\033[m')
elif n <= 14:
    print(f'\033[1mVocê tem {n} anos sua categoria e a \033[m\033[1;35mINFANTIL')
elif n <= 19:
    print(f'\033[1mvocê tem {n} anos sua categoria e a \033[m\033[1;35mJUNIOR\033[m')
elif n == 20:
    print(f'\033[1mVocê tem {n} anos sua categoria e \033[m\033[1;35mSENIOR\033[m')
elif n > 20:
    print(f'\033[1mVocê tem {n} anos sua categoria e a \033[m\033[1;35mMASTER\033[m')
