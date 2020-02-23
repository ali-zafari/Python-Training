from datetime import date

def calculateAge():
    year, month, day = map(int, input().split('/'))
    try:
        born = date(year, month, day)
    except:
        print('WRONG', end='')
        return

    today = date.today()
    print(today.year - born.year - ((today.month, today.day) < (born.month, born.day)), end='')
    
calculateAge()