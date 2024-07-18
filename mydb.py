import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    password = '12345',
    user = 'root'
)

cursorObject = database.cursor()

cursorObject.execute('CREATE DATABASE crm')

print('Completed creating database')