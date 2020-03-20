people = {'name': 'Willian',' sex': 'M', 'age': 23}
print(f'O {people["name"]} has {people["age"]} years old. ')
print()
print(people.keys())
print(people.values())
print(people.items())
print('---' *25)
# del people['sex']             TO REMOVE GENDER
# people['name'] = 'GUSTAVO'    TO CHANGE AN ITEM
for each, v in people.items():          # USING A FOR LOOP TO PRINT ITEMS
    print(f'{each} = {v}')


print('---' * 25)
usa = []        #CREATING A LIST AND ADDING DICTIONARIES
state1 = {'STATE' : 'California', 'sigla': 'CA'}
state2 = {'STATE' : 'Georgia', 'sigla': 'GA'}
usa.append(state1)
usa.append(state2)
print(usa)
print()

estado = dict()
brasil = list()
for  c in range(0,3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['sig']= str(input('Sigla do Estado:'))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    for k, v in e.items():      # k = key | v = value | e.items = dictionarie
        print(f'O campo {k} tem o valor {v}')
print('___' * 25)
