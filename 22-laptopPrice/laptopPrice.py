laptopNum = int(input())

laptopsList = []
#print(type(laptopsList))
for i in range(0, laptopNum) :
    inputStr = str(input())
    mylist = inputStr.split()
    mylist = list(map(int, mylist))
    laptopsList.append(mylist)
laptopsList.sort()
#print(laptopsList)

irsaHappy = False
#algorithm
for i in laptopsList :
    for j in laptopsList :
        if ((i[0] < j[0]) and (i[1] > j[1])) :
            irsaHappy = True

if irsaHappy == True :
    print("happy irsa")
else :
    print("poor irsa")