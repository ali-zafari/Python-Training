intpuStr = str(input())

upperNumber = 0
for letter in intpuStr:
    if letter.isupper():
        upperNumber = upperNumber + 1


if upperNumber > (len(intpuStr)-upperNumber):
    print(intpuStr.upper())
else:
    print(intpuStr.lower())