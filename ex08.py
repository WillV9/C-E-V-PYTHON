#                       Desafio 90
#   Faca um programa que leia NOME e MEDIA de um aluno, guardando tambem a SITUACAO em um DICIONARIO
#   no final, mostre o conteudo da estrutura na tela

school = list()
sit = dict()
sit["NAME"] = str(input('Name of Student: '))
sit["GPA"] = float(input(f'What is the G.P.A of {sit["NAME"]}: '))
sit["RESULT"] =  "APROVED" , "REPROVED" , 'P.P'
if sit["GPA"] < 6:
    sit["RESULT"] = "REPROVED"
elif 6.1 <= sit["GPA"]  <7 :
    sit["RESULT"] = 'P.P'
elif sit["GPA"] >= 7:
    sit["RESULT"] = "APROVED"
school.append(sit.copy())
print("___" *20)
print(f'  Student : {sit["NAME"]} \n  G.P.A is {sit["GPA"]} \n  Final Result is {sit["RESULT"]}')
print("___" *20)

'''  Another option is :    
for k, v in sit.items():
    print(f'    -{k} is equal to {v}   
'''
