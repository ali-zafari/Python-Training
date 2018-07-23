age = 0
oldestAge = 0
olderAge = 0

while age != -1:
    age = int(input())
    if age >oldestAge:
        olderAge = oldestAge
        oldestAge = age

print(oldestAge, olderAge)