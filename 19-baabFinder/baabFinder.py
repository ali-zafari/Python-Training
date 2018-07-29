inputStr = str(input()).lower()

if inputStr.find('ab') != -1 and inputStr.find('ba') != -1 and inputStr.find('bab') == -1 and inputStr.find('aba') == -1 :
    print('YES')
else:
    print('NO')