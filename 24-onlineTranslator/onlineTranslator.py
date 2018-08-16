dictSize = int(input())

artaDict = {}

for i in range(0, dictSize) :
    inputStr = str(input())
    artaDict[inputStr.split()[0]] = inputStr.split()[1]
#print(artaDict)

sentence = (str(input())).split()
translatedSentence = []

for word in sentence :
    translatedSentence.append(artaDict.get(word, word))

print(' '.join(translatedSentence))

