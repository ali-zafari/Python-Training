import hashlib
import csv

def hash_password_hack(input_file_name, output_file_name):
    myHashDatabase = {}
    for i in range(0, 10000) :
        myHashDatabase[hashlib.sha256(str(i).encode('utf-8')).hexdigest()] = i

    with open(input_file_name, newline='') as fRead:
        reader = csv.reader(fRead)
        hashes = []
        for row in reader:
            hashes.append([row[0], row[1]])

    with open(output_file_name, 'w') as fWrite:
        i = 0
        for user, user_hash in hashes :
            if user_hash in myHashDatabase :
                fWrite.write( str(user) + ',' + str('%04d'%(myHashDatabase[user_hash])) )
            i = i + 1
            if(i != len(hashes)):
                fWrite.write('\n')
        fWrite.close()
    return
