def ommitPlusAndSort(rawStr):
    rawStr = rawStr.replace('+', '')
    temp = sorted(rawStr)
    return ''.join(temp)


inputStr = str(input())
sortedStr = ommitPlusAndSort(inputStr)
finalStr = ''

for i in range(0, len(sortedStr)-1):
    finalStr = finalStr + sortedStr[i] + '+'
if len(sortedStr) != 0:
    finalStr = finalStr + sortedStr[len(sortedStr)-1]

print(finalStr)