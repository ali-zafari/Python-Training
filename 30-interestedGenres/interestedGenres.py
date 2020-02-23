peopleNum = int(input())

genres = {'Horror' : 0, 'Romance' : 0, 'Comedy' :0, 'History' : 0 , 'Adventure' : 0 , 'Action' : 0}

for i in range(peopleNum):
    inputGenres = list(filter(lambda x: x in genres.keys(), input().split(' ')))
    for genre in inputGenres:
        try:
            genres[genre] += 1
        except:
            continue

valueSotedThenKeySorted = [v[0] for v in sorted(genres.items(), key = lambda item: (-item[1], item[0]))]

for genre in valueSotedThenKeySorted:
    print( '%s : %d' %(genre, genres[genre]) )