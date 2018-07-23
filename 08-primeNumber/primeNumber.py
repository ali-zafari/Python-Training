a = int(input())
aDivider = a-1

while aDivider > 1:
    if a%aDivider == 0:
        break
    aDivider = aDivider - 1
if aDivider == 1:
    print('prime')
else:
    print('not prime')