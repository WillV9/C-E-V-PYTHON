#               DESAFIO 106
#   Make a mini-system that use  Interactive Help from Python.  The user will type the COMAND and the manuel will appear
# Whenever the user type the word END, the program should finish    |USE COLORS|
c = ('\033[m',                  #_0 - no collors
     '\033[0;20;41m',           #_1 - red
     '\033[0;30;42m',           #_2 - green
     '\033[0;30;43m',           #_3 - yellow
     '\033[0;30;44m',           #_4 - blue
     '\033[0;30;45m',           #_5 - purple
     '\033[7;30m'               #_6 - white
     );


def support(com):
    title(f'Welcome to the command manual \'{com}\'', 5)
    print(c[6], end='')
    help(com)
    print(c[0], end='')


def title(msg, collor):
    size = len(msg) + 4
    print(c[collor], end='')
    print('-='* size)
    print(f'            {msg}')
    print('-=' * size)
    print(c[0], end='')


comand = ''
while True:
    title('_____PyHELP_____', 4)
    comand = str(input('Function or Library :'))
    if comand.upper() == 'END':
        break
    else:
        support(comand)
