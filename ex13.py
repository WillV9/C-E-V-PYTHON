#                       DESAFIO 94
#   Crie um programa que leia NOME , SEXO e IDADE de varias pessoas, Guardando os dados de cada pessoa em um DICIONARIO
#   todos os dicionarios em uma _LISTA_ MOSTRANDO :
#  A) Quantas pessoas foram cadastadas
#  B) A MEDIA de idade do grupo
#  C) Uma lista com todas as MULHERES
#  D) Uma lista com todos as pessoas com IDADE acima da MEDIA

dados = dict()
infoG = list()
sum =  med = 0
while True:
    dados.clear()
    dados["NAME"] = str(input('Name: '))
    while True:
        dados["GENDER"] = str(input('Gender: [M/F]')).strip().upper()[0]
        if dados["GENDER"] in "MF":
            break
        print('Input Invalid. TRY AGAIN [M/F]')
    dados["AGE"] = int(input('Age: '))
    sum += dados["AGE"]
    infoG.append(dados.copy())
    while True:
        ans = str(input('Would You Like to Continue? [Y/N]')).strip().upper()[0]
        if ans in 'YN':
            break
        print('Invalid Input! [Y or N]')
    if ans == 'N':
        break
print('===' * 25)
print(f" list is {infoG}")
print('---' * 25)
print(f'    [A] The total of members registered is {len(infoG)}.')
med = sum / len(infoG)
print(f'    [B] The Average of age from this group is {med}')
print(f'    [C] The Group of Women if formed by: ' , end='')
for e in(infoG):
    if e['GENDER'] == 'F':
        print(f'{e["NAME"]}', end=' ')
print()
print(f'    [D] The list of persons older than average is: ' , end='')
for c in(infoG):
    if c['AGE'] >= med:
        print(f'{c["NAME"]} with {c["AGE"]} Years old.', end=' ')
print('\n=-=-=-=-=-==-=-=-=-==-=-=-=-=> END <=-=-=-=-==-=-=-=-==-=-=-=-=-=')
