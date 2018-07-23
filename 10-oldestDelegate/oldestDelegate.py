age = 0
oldestAge = 0

while age != -1:
    age = int(input())
    if age >oldestAge:
        oldestAge = age

print(oldestAge)