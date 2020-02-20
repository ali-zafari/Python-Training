class student:
    def __init__(self, age, height, weight):
        self.age = age
        self.height = height
        self.weight = weight

    def get_info(self):
        return self.age, self.height, self.weight

classA_num = int(input())
classA = []
agesA = list(map(int, input().split(' ')))
heightA = list(map(int, input().split(' ')))
weightA = list(map(int, input().split(' ')))
for i in range(classA_num):
    temp_class = student(agesA[i], heightA[i], weightA[i])
    classA.append(temp_class)

classB_num = int(input())
classB = []
agesB = list(map(int, input().split(' ')))
heightB = list(map(int, input().split(' ')))
weightB = list(map(int, input().split(' ')))
for i in range(classB_num):
    temp_class = student(agesB[i], heightB[i], weightB[i])
    classB.append(temp_class)


ageAmean = 0.0
heightAmean = 0.0
weightAmean = 0.0
for i in range(classA_num):
    age, height , weight = classA[i].get_info()
    ageAmean += age
    heightAmean += height
    weightAmean += weight

ageAmean = ageAmean/classA_num
heightAmean = heightAmean/classA_num
weightAmean = weightAmean/classA_num

ageBmean = 0.0
heightBmean = 0.0
weightBmean = 0.0
for i in range(classB_num):
    age, height , weight = classB[i].get_info()
    ageBmean += age
    heightBmean += height
    weightBmean += weight

ageBmean = ageBmean/classB_num
heightBmean = heightBmean/classB_num
weightBmean = weightBmean/classB_num

print(ageAmean)
print(heightAmean)
print(weightAmean)
print(ageBmean)
print(heightBmean)
print(weightBmean)

if(heightAmean > heightBmean):
    print('A', end = '')
elif(heightAmean < heightBmean):
    print('B', end = '')
else:
    if(weightAmean < weightBmean):
        print('A', end = '')
    elif(weightAmean > weightBmean):
        print('B', end = '')
    else:
        print('Same', end = '')