import math

numOfNum = int(input())

myNumbers = []
for i in range(0, numOfNum) :
    myNumbers.append(float(input()))

#print(myNumbers)
for number in myNumbers :
    #myNumbers[i] = math.sqrt(myNumbers[i])
    x = int(math.sqrt(number) * 10**4) / 10**4
    print("{:.4f}".format(x))
    #print(str(math.sqrt(number)))
#print(myNumbers)