import re

email = input()

if(re.search(r'^\w+\@[a-zA-Z]+\.[a-zA-Z]+$', email) == None):
    print('WRONG')
else:
    print('OK')
