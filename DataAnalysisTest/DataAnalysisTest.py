import mysql.connector

host= "localhost"
user= "root"
password= "shinratensei1"
database= "testdw"

connection = mysql.connector.connect (host=host, user=user, password=password, database=database)

cursor=connection.cursor()

query= "SELECT * FROM CustomerDimension"

cursor.execute(query)

result=cursor.fetchall()

for row in result:
    print(row)
    
cursor.close()
connection.close()