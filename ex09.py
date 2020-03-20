#               DESAFIO 91
#   Crie um programa onde 4 JOGADORES jogue um DADO e tenham resultados ALEATORIOS. guarde esses resultados em um
#   DICIONARIO. no final coloque esse dicionario em ORDEM, Sabendo que o Vencedor tirou o maior numero no DADO

from random import randint
from time import sleep
from operator import itemgetter

players = {'Player1': randint(1, 6),
           'Player2': randint(1, 6),
           'Player3': randint(1, 6),
           'Player4': randint(1, 6)}
ranking = list()
print('Loading... ')
sleep(1.5)
for k, v in players.items():
    print(f"The {k} got #{v} ")
    sleep(1)
ranking = sorted(players.items(), key=itemgetter(1), reverse=True)
print('-=' * 5 ,'RANKING','-=' * 5)
for i, v in enumerate(ranking):
    print(f'{i+1}`Place: {v[0]} with {v[1]}pts.')
    sleep(0.7)
print('-=' * 15)


