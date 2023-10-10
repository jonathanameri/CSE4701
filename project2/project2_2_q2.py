import mysql.connector
import pymongo

# Connect to mySQL
my_db = mysql.connector.connect(
    host= "localhost",
    user= "root",
    password= "", database= "order_db") 
    
cursor = my_db.cursor()

# connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = "warehouse"
mydb = client[db]

# specify the collection (collection is a table in the database)
mycol = mydb["images"]

docs = mycol.find()

for doc in docs:
    city = doc["address"].split(",")[1].strip()
    sql = "UPDATE WAREHOUSE SET City = %s WHERE name = %s"
    val = (city, doc["name"])
    cursor.execute(sql, val)
my_db.commit()

cursor.close()
exit(0)


