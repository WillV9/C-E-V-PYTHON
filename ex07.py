#               DESAFIO 89
#   Crie um programa que leia o NOME e DUAS NOTA  de varios alunos e guarde tudo em uma lista composta. No final, mostre
#   um boletim contendo a MEDIA  de cada um e permita que o usuario possa mostrar as notas de cada aluno individualmente

rform = list()      #   REGISTRATION FORM
while True:
    name = str(input('Name : '))
    grade1 =  float(input('1st Grade : '))
    grade2 = float(input('2nd Grade : '))
    med = (grade1 + grade2) / 2
    rform.append([name, [grade1, grade2], med])   # G.P.A
    ans = str(input('Would You Like to Continue? [Y/N]')).strip().upper()[0]
    if ans == 'N':
        break
print("'''" * 20)
print(f'{"No.":<5}{"NAME":<10}{"GPA":>8}')
print("'''" * 20)
for n,m in enumerate(rform):
    print(f'{n:<5}{m[0]:<10}{m[2]:>8.1f}')
print("'''" * 20)
while True:
    ShowMed = int(input('Which student  transcrip you want to see? [999 to END]: '))
    if ShowMed == 999:
        print('Finalizing program...')
        break
    if ShowMed <= len(rform) - 1:
        print(f'The Grades of Student :{rform[ShowMed][0]} were {rform[ShowMed][1]}\n')
print('Thank You for using our Platform..')
