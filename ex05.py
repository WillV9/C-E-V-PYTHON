#                      DESAFIO 78
# Faca um programa que leia 5 valores numericos e guarde os em uma lista
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectvas posicoes na lista

cont = bigger = smaller = 0
values = list()
for each in range(0, 5):
    values.append(int(input(f'Please Insert Value in position {each}:')))
    if each == 0:
        bigger = smaller = values[each]
    else:
        if values[each] > bigger:
            bigger = values[each]
        if values[each] < smaller:
            smaller = values[each]
print('~~~~~' * 14)
print(f'The Biggest Number is {bigger} , at position', end='')
for a, pos in enumerate(values):
    if pos == bigger:
        print(f' {a} ;', end='')
print()
print(f'\nThe smallest number is {smaller} , at position ', end='')
for a, pos in enumerate(values):
    if pos == smaller:
        print(f'{a} ..\n')

print(f"You've Typed The Following Numbers => {values}")

'''         THIS IS ANOTHER VERSION OF THE SAME PROGRAM - 
lista = []
maior = []
menor = []
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para posição {c}: ')))
print(f'Você digitou os valores {lista}')
for i, v in enumerate(lista):
    if v == max(lista):
        maior.append(i)
    if v == min(lista):
        menor.append(i)
print(f'O maior valor digitado foi {max(lista)} na posição {maior}')
print(f'O menor valor digitado foi {min(lista)} na posição {menor}')

'''
