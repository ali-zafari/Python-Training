playersNum = int(input())

inputStr = str(input())
matchesPlayed = inputStr.split()
matchesPlayed = list(map(int, matchesPlayed))

qualifiedPlayersNum = 0
for player in matchesPlayed:
    if player <= 2 :
        qualifiedPlayersNum = qualifiedPlayersNum + 1
teamsNum = int(qualifiedPlayersNum/3)
print(teamsNum)