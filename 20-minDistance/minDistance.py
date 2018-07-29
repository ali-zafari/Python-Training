inputStr = str(input())
mylist = inputStr.split()
mylist = list(map(int, mylist))
mean = sum(mylist)/3

minDistance = 0
for element in mylist:
    minDistance = minDistance + abs(element-mean)

print('%g' %minDistance)