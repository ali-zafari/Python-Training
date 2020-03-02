peopleNum = int(input())

f_dict = {}
m_dict = {}

for i in range(peopleNum):
    list_input = input().split('.')
    if( list_input[0] == 'f' ):
        f_dict[list_input[1].title()] = list_input[2]
    elif( list_input[0] == 'm' ):
        m_dict[list_input[1].title()] = list_input[2]

for key in sorted(f_dict.keys()):
    print( 'f %s %s' %(key, f_dict[key]) )

for key in sorted(m_dict.keys()):
    print( 'm %s %s' %(key, m_dict[key]) )