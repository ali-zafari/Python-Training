
import mysql.connector

cnx = mysql.connector.connect(user='root', password='*MYSQL*password',
                              host='127.0.0.1',
                              database='test')

cursor = cnx.cursor()
select_command = 'SELECT * FROM employeesTable;'
cursor.execute(select_command)

selectedData = cursor.fetchall()

#stored data is formatted as: [ (name, weight, height) ]
selectedData.sort(key = lambda x : (x[2], -1*x[1]), reverse = True)

for name, weight , height in selectedData:
    print(name, height, weight)

cnx.close()