class human:
    def __init__(self, name):
        self.name = name

class footballer(human):
    def __init__(self, name, team):
        human.__init__(self , name)
        self.team = team
    def introduce(self):
        print(self.team, ': ', self.name)

import random

#22 footballer names:
names_list = ['hasan', 'maziar', 'akbar', 'nima', 'mehdi', 'frahad', 'mohamad', 'khashayar', 'milad', 'mostafa', 'amin', 'saeed', 'puya', 'puria', 'reza', 'ali', 'behzad', 'soheil', 'behruz', 'shahruz', 'saman', 'mohsen']
#numbers from 0 to 21:
num_list = [x for x in range(22)]
#shuffling the numbers randomly:
random.shuffle(num_list)

footballers_list = []
for i in range(21):
    if( i < 11 ):
        footballers_list.append(footballer(names_list[num_list[i]], 'A'))
    else:
        footballers_list.append(footballer(names_list[num_list[i]], 'B'))

for footbalist in footballers_list:
    footbalist.introduce()

