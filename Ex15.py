# cook your dish here
#               desafio 99
from time import sleep


def bigger(* num):
    cont = bigger = 0
    print('-='*3 , "Analizing Order of Numbers", '=-'*3)
    for e in num:
        print(f'{e}' , end=' ')
        sleep(0.8)
        if e == 0:
            bigger = e
        else:
            if e > bigger:
                bigger = e
        cont += 1 
    print(f'\nThe Biggest Number of this list is : {bigger}')
        
        
bigger(6,9,13,2,8,14,31,2,5,22)
bigger(9,15,3,21,4,17,1,12)
bigger(4,8,12,10,7,5,19)
bigger(5,15,29,46,33)
