def numOfDivisors(x):
    output = 0
    xDivider = x
    while xDivider >= 1:
        if (x % xDivider) == 0:
            output = output + 1
        xDivider = xDivider - 1
    return output

# while True:
#     a = int(input())
#     print(numOfDivisors(a))
a = 0
for i in range(0, 20):
    newNumber = int(input())
    if numOfDivisors(newNumber) > numOfDivisors(a):
        a = newNumber
    elif numOfDivisors(newNumber) == numOfDivisors(a):
        if newNumber > a:
            a = newNumber

print(a, numOfDivisors(a))