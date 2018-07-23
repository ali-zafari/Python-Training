def letterIsConsonant(letterUnderTest) :
    consonants = 'bcdfghjklmnpqrstvwxyz'
    if letter in consonants:
        return True
    else:
        return False


inputStr = str(input())

inputStr = inputStr.lower()
inputStr = inputStr.replace('a', '')
inputStr = inputStr.replace('e', '')
inputStr = inputStr.replace('i', '')
inputStr = inputStr.replace('o', '')
inputStr = inputStr.replace('u', '')

outputStr = ''
for letter in inputStr:
    if(letterIsConsonant(letter)):
        outputStr = outputStr + '.'
    outputStr = outputStr + letter

print(outputStr)