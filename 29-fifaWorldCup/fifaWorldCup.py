def teams_indices(line_number):
    if(line_number == 0):
        team1 = 0
        team2 = 1
    elif(line_number == 1):
        team1 = 0
        team2 = 2
    elif(line_number == 2):
        team1 = 0
        team2 = 3
    elif(line_number == 3):
        team1 = 1
        team2 = 2
    elif(line_number == 4):
        team1 = 1
        team2 = 3
    elif(line_number == 5):
        team1 = 2
        team2 = 3
    return team1, team2

def sort_indices():
    temp_points = points.copy()
    max_indices = []

    for i in range(4):
        max_indices.append(temp_points.index(max(temp_points)))
        temp_points[temp_points.index(max(temp_points))] = -1
    
    for j in range(3):
        for i in range(3):
            if( points[max_indices[i]] == points[max_indices[i+1]] ):
                if( wins[max_indices[i]] < wins[max_indices[i+1]] ):
                    temp = max_indices[i]
                    max_indices[i] = max_indices[i+1]
                    max_indices[i+1] = temp
                elif( wins[max_indices[i]] == wins[max_indices[i+1]] ):
                    if(indices_to_name[max_indices[i]][0] > indices_to_name[max_indices[i+1]][0] ):
                        temp = max_indices[i]
                        max_indices[i] = max_indices[i+1]
                        max_indices[i+1] = temp 

    return max_indices


#iran:0, spain:1, portugal:2, morocco:3
indices_to_name = {0: 'Iran', 1:'Spain', 2:'Portugal', 3:'Morocco'}
wins = [0, 0, 0, 0]
loses = [0, 0, 0, 0]
draws = [0, 0, 0, 0]
points = [0, 0, 0, 0]
goal_diff = [0, 0, 0, 0]

for i in range(6):
    input_string = input()
    team1goal = int(input_string.split('-')[0])
    team2goal = int(input_string.split('-')[1])
    team1, team2 = teams_indices(i)
    if(team1goal > team2goal):
        wins[team1] = wins[team1] + 1
        loses[team2] = loses[team2] + 1
    elif(team1goal < team2goal):
        wins[team2] = wins[team2] + 1
        loses[team1] = loses[team1] + 1
    else:
        draws[team1] = draws[team1] + 1
        draws[team2] = draws[team2] + 1
    goal_diff[team1] = goal_diff[team1] + team1goal - team2goal
    goal_diff[team2] = goal_diff[team2] + team2goal - team1goal

for i in range(len(points)):
    points[i] = 3*wins[i] + draws[i]

sorted_indices = sort_indices()

for i in sorted_indices:
    print("%s  wins:%d , loses:%d , draws:%d , goal difference:%d , points:%d"
     %(indices_to_name[i], wins[i], loses[i], draws[i], goal_diff[i], points[i]))