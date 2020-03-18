#                   DESAFIO 84
#   Faca um programa que leia o NOME E PESO de varias pessoas. guardando tudo em uma lista. No final mostre
#  A) QUANTAS pessoas foram cadastradas.
#  B) Uma listagem com as pessoas mais PESADAS.
#  C) Uma listagem com os pessoas mais LEVES.

rsearch = list()
data = list()
fatty = skinny = 0
print('==='* 30)
while True:
    name = str(input('Name : '))
    wei = float(input('Weight : '))
    rsearch.append(name)
    rsearch.append(wei)
    data.append(rsearch[:])
    rsearch.clear()
    ans = ' '
    while ans not in 'YN':
        ans = str(input('Would you like to add another person ? [Y/N]')).strip().upper()[0]
    if ans == 'N':
        break
print('-----' *30)
print(f'\nIn Total there was {len(data)} persons registered in this Research!')
for e in data:
    if e[1] > 100:
        print(f'{e} ', end='')
        print('This group is most likely OverWeight')
for e in data:
    if e[1] < 50:
        print(f'The group formed by {e} ',end='')
        print('is Probably Underweight')
