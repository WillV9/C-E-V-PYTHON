#               DESAFIO 103
# Create a Programa that has a FUNCTION called_  record() receiving than Two Optional Parameters :
# Name of player and  how many GOALS scored.
# The programa should be able to show the Player record even if the user did not input any information

def record(nam='<unknown>', point=0):
    print('=-'* 9, "  PLAYER STATS  ",'-=' *9)
    print(f'Player {nam} has scored {point} Time(s) during this season! ')

n = str(input('Player Name: '))
g = str(input('How many [Goals/Points] scored: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    record(point=g)
else:
    record(n, g)
    
 #----------------------------------------------------------------------------------------------------------
#               DESAFIO 104
# Make a programa that has a FUNCTION : readint() , it will work like the function input() but just doing the VALIDATION
# To accept only one numeric value      EX: n = readint("Type a n")


def readint(num):
    ok = False
    value = 0
    while True:
        n = str(input(num))
        if n.isnumeric():
            value = int(n)
            ok = True
        else:
            print('\033[0;31m ERROR! INVALID INPUT. Type a Integer Number\033[m')
        if ok:
            break
    return value


n = readint('Type a Number: ')
print(f"You've just typed number {n}")

