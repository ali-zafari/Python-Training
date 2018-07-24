inputStr = str(input()).lower()

if inputStr == ''.join(reversed(inputStr)):
    print('palindrome')
else:
    print('not palindrome')