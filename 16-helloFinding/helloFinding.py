inputStr = str(input()).lower()

cleanedStr = inputStr[0]

for letter in inputStr:
    if letter != cleanedStr[len(cleanedStr)-1]:
        cleanedStr = cleanedStr + letter
    elif letter == 'l' and cleanedStr[len(cleanedStr)-1] and cleanedStr[len(cleanedStr)-2] != 'l':
        cleanedStr = cleanedStr + letter

if cleanedStr.find('hello') != -1:
    print('YES')
else:
    print('NO')