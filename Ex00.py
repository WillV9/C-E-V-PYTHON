#                  Desafio 41
#   Crie um programa que classifique the age category of athletes base in their Year of Birthday..

from datetime import date
actual = date.today().year
print('Hello There the San Mateo Swimming Association Try outs will be happening in April 2020:')
print('Are you interested in Join Team ?')
bdayear = int(input('If you are , please type your year of Birthday:'))
age = actual - bdayear
if age <= 9:
    print('You will be in the lil category.')
elif age <= 14:
    print('You will be in the infant category.')
elif age <=19:
    print('You will be in the Junior category.')
elif age <= 25:
    print('You will be in the Senior category.')
else:
    print('You are in the Master category.')
