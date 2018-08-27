import csv
# For the average
from statistics import mean 

def calculate_averages(input_file_name, output_file_name):
    with open(input_file_name, newline='') as fRead:
        reader = csv.reader(fRead)
        averages = {}
        for row in reader:
            averages[row[0]] = float(mean(map(int, row[1:])))
        
    with open(output_file_name, 'w') as fWrite:
        for key, value in averages.items():
            fWrite.write(str(key) + ',' + str(value))
            if((list(averages.keys())[-1] != key) and (list(averages.values())[-1] != value) ):
                fWrite.write('\n')
        fWrite.close()
    return

def calculate_sorted_averages(input_file_name, output_file_name):
    with open(input_file_name, newline='') as fRead:
        reader = csv.reader(fRead)
        averages = {}
        for row in reader:
            averages[row[0]] = float(mean(map(int, row[1:])))

    with open(output_file_name, 'w') as fWrite:
        for key, value in sorted(averages.items(), key=lambda x:x[1]):
            fWrite.write(str(key) + ',' + str(value))
            if( (sorted(averages.items(), key=lambda x:x[1])[-1][0] != key) and (sorted(averages.items(), key=lambda x:x[1])[-1][1] != value) ):
                fWrite.write('\n')
        fWrite.close()
    return

def calculate_three_best(input_file_name, output_file_name):
    with open(input_file_name, newline='') as fRead:
        reader = csv.reader(fRead)
        averages = {}
        for row in reader:
            averages[row[0]] = float(mean(map(int, row[1:])))
    
    sortedAverages = sorted(averages.items(), key=lambda x:x[1])
    if len(sortedAverages) >= 3 :
        rangeOfBests = -4
    elif len(sortedAverages) == 2 :
        rangeOfBests = -3
    elif len(sortedAverages) == 1 :
        rangeOfBests = -2
    else :
        rangeOfBests = 0

    with open(output_file_name, 'w') as fWrite:
        for i in range(-1, rangeOfBests, -1):
            fWrite.write( str(sortedAverages[i][0]) + ',' + str(sortedAverages[i][1]) )
            if(i != (rangeOfBests + 1)):
                fWrite.write('\n')
        fWrite.close()
    return

def calculate_three_worst(input_file_name, output_file_name):
    with open(input_file_name, newline='') as fRead:
        reader = csv.reader(fRead)
        averages = {}
        for row in reader:
            averages[row[0]] = float(mean(map(int, row[1:])))

    sortedAverages = sorted(averages.items(), key=lambda x:x[1])
    if len(sortedAverages) >= 3 :
        rangeOfWorsts = 3
    elif len(sortedAverages) == 2 :
        rangeOfWorsts = 2
    elif len(sortedAverages) == 1 :
        rangeOfWorsts = 1
    else :
        rangeOfWorsts = -1

    with open(output_file_name, 'w') as fWrite:
        for i in range(0, rangeOfWorsts, 1):
            fWrite.write(str(sortedAverages[i][1]))
            if(i != (rangeOfWorsts - 1)):
                fWrite.write('\n')
        fWrite.close()
    return
def calculate_average_of_averages(input_file_name, output_file_name):
    with open(input_file_name, newline='') as fRead:
        reader = csv.reader(fRead)
        averages = {}
        for row in reader:
            averages[row[0]] = float(mean(map(int, row[1:])))

    with open(output_file_name, 'w') as fWrite: 
        if(len(averages) > 0) :
            fWrite.write(str(float(mean(averages.values()))))
        fWrite.close()
    return
