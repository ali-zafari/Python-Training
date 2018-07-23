points = 0
wins = 0
for i in range(0, 30):
    newPoint = int(input())
    points = points + newPoint
    if(newPoint == 3):
        wins = wins + 1
print(points, wins)