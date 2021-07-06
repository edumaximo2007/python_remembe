import emoji
from random import randint
print('=-='*10)
print('''\033[7m         DESAFIO 058         \033[m''')
print('=-='*10)
print(emoji.emojize(''':bulb: \033[1mMelhore o jogo do \033[m\033[1;32mDESAFIO028\033[m\033[1m onde o computador vai
"pensar" em um \033[m\033[1;35mnúmero entre 0 e 10\033[m\033[1m. Só que agora o jogador vai tentar adivinhar até acertar
mostrando no final quantos palpites foram necessários para vencer\033[m''', use_aliases=True))
print('')
print('\033[7mJOGO DA ADVINHAÇÃO\033[m')
print('')
print('\033[1mTente adivinhar o número que eu estou pensando de 0 a 10...\033[m')
print('')
pc = randint(0, 10)
contador = 0
jogador = int(input('\033[1mDigite um número: '))
print('')
while pc:
    if pc == jogador:
        print('\033[1mAcertou miseravi\033[m')
        break
    else:
        contador += 1
        jogador = int(input('\033[1mDigite um número:\033[m '))
print(f'\033[1mVocê precisou jogar {contador}x para me vencer\033[m')

