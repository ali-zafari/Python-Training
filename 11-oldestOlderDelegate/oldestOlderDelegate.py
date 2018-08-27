age = 0
oldestAge = 0
olderAge = 0

while age != -1:
    age = int(input())
    if age >oldestAge:
        olderAge = oldestAge
        oldestAge = age
if (oldestAge != 0) and (olderAge != 0) :
    print(oldestAge, olderAge)
elif (olderAge == 0) and (oldestAge != 0) :
    print(oldestAge)