numOfNames = 2
names = ['', '', '', '', '', '', '', '', '', '']

for i in range(0, numOfNames):
    names[i] = str(input()).lower()



for i in range(0, numOfNames):
    if len(names[i]) != 0:
        names[i] = names[i][0].upper() + names[i][1:]
    print(names[i])

