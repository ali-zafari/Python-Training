def isPrime(x):
    if(x>1):
        xDivider = x-1
        while xDivider > 1:
            if (x % xDivider) == 0:
                return False
            xDivider = xDivider - 1
        return True
    return False

def numOfPrimeDivisors(x):
    output = 0
    xDivider = x
    while xDivider >= 1:
        if (x % xDivider == 0 and isPrime(xDivider) == True):
            output = output + 1
        xDivider = xDivider - 1
    return output

numbers_dict = {}
for i in range(10):
    number = int(input())
    numbers_dict[number] = numOfPrimeDivisors(number)

key_max = max(numbers_dict, key=numbers_dict.get)
value_max = numbers_dict[key_max]

for key, value in numbers_dict.items():
    if(value == value_max):
        if(key > key_max):
            key_max = key

print(key_max, numbers_dict[key_max])
