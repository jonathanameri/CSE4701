import mysql.connector
import pymongo


my_db = mysql.connector.connect(
    host= "localhost",
    user= "root",
    password= "", database= "order_db") 
    
cursor = my_db.cursor()

# delete old warehouse table
cursor.execute("ALTER TABLE SHIPMENT DROP CONSTRAINT shipment_ibfk_2")
cursor.execute("DROP TABLE WAREHOUSE")

# create new warehouse table
sql = "CREATE TABLE WAREHOUSE (Warehouse_No VARCHAR(255), Name VARCHAR(255), City VARCHAR(255), PRIMARY KEY (Warehouse_No))"
cursor.execute(sql)

sql = "INSERT INTO WAREHOUSE (Warehouse_No, Name, City) VALUES (%s, %s, %s)"
values = (("W1", "Husky Vernon", ""),("W2", "Target LA", ""),("W3", "Bobs Phoenix", ""),("W4", "Costco Houston", ""),("W5", "Best Buy Miami", ""))
cursor.executemany(sql, values)

cursor.execute("SELECT * FROM WAREHOUSE")
print(cursor.fetchall())
my_db.commit()

cursor.close()