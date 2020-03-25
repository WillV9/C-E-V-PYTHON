#                   DESAFIO 99
#   FACA UM PROGRAMA QUE TENHA UMA FUNCAO CHAMADA MAIOR(), QUE RECEBA VARIOS PARAMETROS COM VALORES INTEIROS.
#   SEU PROGRAMA TEM QUE ANALISAR TODOS OS VALORES E DIZER QUAL E MAIOR
from time import sleep
from random import randint


def bigger(* num):
    cont = bigger = 0
    print('-->'* 4, "SCANNING NUMBERS", '<--'*4)
    for each in num:
        print(f'{each} ', end=" ")
        sleep(0.5)
        if each == 0:
            bigger = each
        else:
            if each > bigger:
                bigger = each
        cont += 1
    print(f'\nBetween {cont} numbers, The Biggest is = {bigger}')
    print('-'* 42)
    sleep(1.2)


bigger(5, 8, 11, 15, 2, 6, 1, 9, 14, randint(1,35))
bigger(19, 16, 11, 17, 3, 7, 4, randint(5,29))
bigger(21, 13, 6, 7, 11, 8, randint(11,22))
bigger(102,95,147,56, randint(39, 150))
bigger(34, 49,28, randint(1,55))
