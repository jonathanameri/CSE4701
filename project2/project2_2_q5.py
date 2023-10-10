import pymongo
import mysql.connector

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

cmd = """SELECT DISTINCT WAREHOUSE.Name
FROM SHIPMENT
JOIN `ORDER` ON SHIPMENT.order = `ORDER`.order
JOIN WAREHOUSE ON WAREHOUSE.Warehouse_no = SHIPMENT.warehouse
WHERE DATEDIFF(SHIPMENT.ship_date, `ORDER`.ODate) > 30; """

cursor.execute(cmd)

result = cursor.fetchall()
for row in result:
    w = mycol.find_one({"name": row[0]})
    file = open(row[0].replace(" ", "_") + ".pdf", "wb")
    file.write(w["description"])
    file.close()
    
cursor.close()