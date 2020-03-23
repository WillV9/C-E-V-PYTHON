#                   DESAFIO 95
# Aprimore o DESAFIO 93 para que ele funcione com VARIOS JOGAODRES,
# incluindo um sistema de visualizao deDETALHES DE APROVEITAMENTO de cada jogador

player = dict()
goals = list()
team = list()
print('-=' * 30)
while True:
    player.clear()
    player["Name"] = str(input('Name: '))
    GamesPlayed = int(input(f'How many Games {player["Name"]} Played: '))
    goals.clear()
    for each in range(1, GamesPlayed+1):
        goals.append(int(input(f'    Goals Score on game {each}: ')))
    player["GOALS"] = goals[:]
    player["TOTG"] = sum(player["GOALS"])
    average = sum(goals) / GamesPlayed
    team.append(player.copy())
    while True:
        ans = str(input('Would You Like to Continue ? [Y/N]')).strip().upper()[0]
        if ans in 'YN':
            break
        print('Invalid Input!   [Y or N]')
    if ans == 'N':
        print('-=' * 30)
        break
print()
print('==' *40)
print('N.#', end='')
for i in player.keys():
    print(f'{i:<20}', end='')
print()
print('==' * 40)
for key, v in  enumerate(team):
    print(f' {key:>1}', end=" ")
    for d in v.values():
        print(f'{str(d):<20}', end='')
    print()
print('==' * 40)
while True:
    search = int(input('Which Player# Stats do you want to see? [999_END]'))
    if search == 999:
        break
    if search >= len(team):
        print(f' Invalid Input! PLAYER {search} Does Not Exist.')
    else:
        print(f'\n     ____ STATS OF PLAYER ____ {team[search]["Name"]} ')
        for i, g in enumerate(team[search]["GOALS"]):
            print(f'     On Match {i+1} scored {g} Goals.')
        print()
    print('|=|=' * 30)
print('~~~~~> END <~~~~~')
