import emoji
print('=-='*10)
print('''\033[7m          DESAFIO 043         \033[m''')
print('=-='*10)
print(emoji.emojize(''':bulb: \033[1mDesenvolva uma lógica que leia o peso e a altura de uma pessoa, calucle o seu\033[m
\033[1;32m IMC\033[m\033[1m e mostre o seu status, de acordo com a tabela abaixo:\033[m

\033[1;32m-\033[m\033[1m Abaixo de\033[m\033[1;35m 18.5\033[m\033[1m: Abaixo do peso \033[m
\033[1;32m-\033[m\033[1m Entre\033[m\033[1;35m 18.5\033[m\033[1m e \033[m\033[1;35m25\033[m\033[1m: Peso ideal\033[m
\033[1;32m-\033[m\033[1;35m 25\033[m\033[1m até\033[m\033[1;35m 30\033[m\033[1m: Sobrepeso\033[m
\033[1;32m-\033[m\033[1;35m 30\033[m\033[1m até\033[m\033[1;35m 40\033[m\033[1m: Obseidade\033[m
\033[1;32m-\033[m\033[1m Acima de \033[m\033[1;35m40\033[m\033[1m: Obesidade morbida\033[m''', use_aliases=True))
print('')
print('\033[7mÌNDICE DE MASSA CORPORAL\033[m')
print('')
n1 = float(input('\033[1mPeso:\033[m '))
n2 = int(input('\033[1mAltura: '))
imc = n1 / n2 ** 2 * 10000
if imc < 18.5:
    print(f'\033[1mVocê esta abaixo do peso, seu IMC \033[1m\033[1;31m{imc:.1f}\033[m')
elif imc < 25:
    print(f'\033[1mVocê esta no peso ideal seu IMC\033[m\033[1;32m {imc:.1f}\033[m')
elif imc < 30:
    print(f'\033[1mVocê esta com sobrepeso seu IMC\033[m\033[1;31m {imc:.1f}\033[m')
elif imc < 40:
    print(f'\033[1mVocê está com obesidade seu IMC\033[m\033[1;31m {imc:.1f}\033[m')
elif imc > 40:
    print(f'\033[1mVocê esta com obsidade morbida seu IMC\033[m\033[1;31m {imc:.1f}\033[m')
