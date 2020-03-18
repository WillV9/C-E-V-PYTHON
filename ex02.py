'''           DESAFIO 59
   Crie um programa que leia dois valores e mostre um menu na tela:
        [1] somar
        [2] multiplicar
        [3] maior
        [4] novos numeros
        [5] sair do programa
    seu programa devera realizar a operacao solicitada em cada caso! '''
from random import randint
from time import sleep
firstV = int(input('Type the first value:   '))
secondV = int(input('Type the second value: '))
sum = 1
multiply = 2
bigger = 3
newnum = 4
exit = 5
opt = 0
while opt != 5:
    print('=~==~=' * 10)
    opt = int(input(' [1] SUM \n'
                 ' [2] Multiply \n'
                 ' [3] Bigger \n'
                 ' [4] New numbers\n'
                 ' [5] Exit\n   What is your option?'))
    print('=~==~=' * 10)
    if opt == 1:
        print('The SUM between {} and {} is {}'.format(firstV,secondV, firstV + secondV))
    if opt == 2:
        print('The result of {} * {} is {}'.format(firstV, secondV, firstV * secondV))
    if opt == 3:
        if firstV > secondV:
            print('The number {} is bigger than {} '.format(firstV,secondV))
        elif secondV > firstV:
            print('The number {} is bigger than {}'.format(secondV, firstV))
    if opt == 4:
        print('Replace your input numbers:')
        rnum1 = int(input('Type the first new value:'))
        rnum2 = int(input('Type the second new value:'))
        firstV = rnum1
        secondV = rnum2
    if opt == 5:
        print('Finalizing program... ')
        sleep(2)
    elif opt > 5:
        print('INVALID OPTION! Try [1/5]')






