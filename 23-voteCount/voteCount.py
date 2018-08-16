voteNum = int(input())

voteData = {}

for i in range(0, voteNum) :
    inputStr = str(input())
    voteData[inputStr] = voteData.get(inputStr, 0) + 1
#print(sorted(voteData.items()))

for person, votes in sorted(voteData.items()) :
    print(person, votes)