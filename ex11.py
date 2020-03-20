#                   DESAFIO 93
#   Crie um programa que gerencie o aproveitamento de um JOGADOR DE FUTEBOL. O Programa vai ler O NOME DO JOGADOR E
#   QUANTAS PARTIDAS  ele jogou . Depois vai ler a QUANTIDADE DE GOLS feitos em cada partida. No final, tudo isso sera
#   Guardado em um DICIONARIO CADA PARTIDA. No final, tudo isso sera guardado em um DICIONARIO, incluindo TOTAL DE GOLS
#   Feitos durante o campeonato

player = dict()
games = list()
print('===' *15)
player["Name"] = str(input('Footbaler Name: '))
TotGames = int(input('How Many Games Played: '))
cont = 0
for e in range(1,TotGames+1):
    games.append(int(input(f'   Goals Scored on game {e}: ')))
print('===' * 15)
player["Goals"] = games[:]
player["TotalG"] = sum(games)
average = sum(games) / TotGames
print(f'Player {player["Name"]} has scored {player["TotalG"]} Goals in {TotGames} Games \nPlayed with an average '
      f'of {average:.2f} goals per game!')
print('***' * 15)
for e, g in enumerate(games):
    print(f' => On match {e+1}, {player["Name"]} scored {g} Goals.         |')
print('***' * 15)



