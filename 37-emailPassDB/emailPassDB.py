import re
import mysql.connector

def isEmailTrue(email):
    if(re.search(r'^\w+\@[a-zA-Z]+\.[a-zA-Z]+$', email) == None):
        return False
    else:
        return True

def isPassTrue(password):
    if(re.search(r'^\w+$', password) == None):
        return False
    else:
        return True


print('Please enter your email:')
email = input()
print('Please enter your password:')
password = input()

email_condition, pass_condition = False, False

while(email_condition == False or pass_condition == False):
    
    email_condition = isEmailTrue(email)
    pass_condition  = isPassTrue(password)
    
    if(email_condition == False):
        print('Email format is wrong! Enter another email (ex. expression@string.string):')
        email = input()
    if(pass_condition == False):
        print('Password format is wrong! Enter another password (an expression only):')
        password = input()

cnx = mysql.connector.connect(user='root', password='*MYSQL*password',
                              host='127.0.0.1',
                              database='test')
cursor = cnx.cursor()

insert_command = add_employee = ('INSERT INTO userpass (username, password) VALUES (%s, %s);')
cursor.execute(insert_command, (email , password))
cnx.commit()

cursor.close()
cnx.close()