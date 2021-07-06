import emoji
print('=-='*10)
print('''\033[7m          DESAFIO 042         \033[m''')
print('=-='*10)
print(emoji.emojize(''':bulb: \033[1mRefaça o \033[m\033[1;32mDESAFIO 035\033[m\033[1m dos triângulos, acrescentando o
recurso de mostrar que tipo de triângulo será formado:\033[m

\033[1;32m-\033[m\033[1;35m Equilátero\033[m\033[1m: todos os lados iguais\033[m
\033[1;32m-\033[m\033[1;35m Isórceles\033[m\033[1m: dois lados iguais\033[m
\033[1;32m-\033[m\033[1;35m Escaleno\033[m\033[1m: todos os lados diferentes\033[m''', use_aliases=True))
print('')
print('\033[7mANALISANDO TRIÂNGULOS\033[m')
print('')
a = float(input('\033[1mLado\033[m\033[1;35m A\033[m: '))
b = float(input('\033[1mlado\033[m\033[1;37m B\033[m '))
c = float(input('\033[1mLado\033[m\033[1;32m C\033[m '))
if a < b + c and b < a + c and c < a + b:
    print('\033[1mOs números acima podem forma um triângulo\033[m, end)
    if a == b == c:
        print('\033[1;35mEQUILATERO\033[m')
    elif a != b != c != a:
        print('\033[1;35mESCALENO\033[m')
    else:
        print('\033[1;35mISÓRCELES\033[m')
else:
    print('\033[1;31mOs números acima não podem forma um triângulo\033[m')
#if a == b == c:
 #   print(f'\033[1mCom base nos números {a:.0f} x {b:.0f} x {c:.0f}, você acabou de fazer um triângulo\033[m\033[1;35m EQUILATERO\033[m')
#elif a + b > c and b + a > c and c + b > a and a + c > b and c + b > a and c + a > b and b + c > a:
 #   print(f'\033[1mCom base nos números {a:.0f} x {b:.0f} x {c:.0f}, você acabou de fazer um triângulo\033[m\033[1;35m ISORCELES\033[m')
#elif a != b and c !=b and a !=c:
 #   print(f'\033[1mCom base nos números {a:.0f} x {b:.0f} x {c:.0f}, você acabou de fazer um triângulo\033[1;35m ESCALENO\033[m')
#elif (a + b) < c and (b + a) < c and (c + b) < a and (a + c) < b and (c + b) < a and (c + a) < b and (b + c) < a:
 #   print('\033[1mOs números acima não podem forma um triângulo\033[m')
