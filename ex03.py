#           Desafio 68
#   Faca um programa que jogue PAR OU IMPAR com seu computador. o jogo so sera interrompido quando o jogador perder
#   MOSTRE O TOTAL DE VITORIAS CONSECUTIVAS que ele conquistou no final do jogo
from random import randint
Macnum = randint(0,11)
Playrnum = vit = 0
print('____' * 8)
print('Lets Play \033[1;30;45m ODD \033[m or \033[7;30;45m EVEN \033[m')
print('____' * 8)
while True:
    Playrnum = int(input('Type a number: '))
    Macnum = randint(0,11)
    result = Playrnum + Macnum
    type  = ' '
    while type not in 'OE':
        type = str(input('ODD or EVEN? [O/E]')).strip().upper()[0]
    print(f'You played {Playrnum} and the machine played {Macnum} , the total is {result}...', end='')
    print('Its an EVEN#' if result % 2== 0 else 'It is an ODD#')
    if type == 'E':
        if result % 2 == 0:         # LOGIC FOR EVEN NUMBERS
            print('Your Win , Keep Playing..')
            vit += 1
        else:
            print('You Lost.')
            break
    elif type == 'O':
        if result % 2 == 1:         # LOGIC FOR ODD NUMBERS
            print('Your Win , Keep Playing..')
            vit += 1
        else:
            print('You lost.')
            break
print(f'You Won {vit} times.')
