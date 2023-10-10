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

cmd = """SELECT WAREHOUSE.name 
FROM WAREHOUSE 
JOIN SHIPMENT ON WAREHOUSE.Warehouse_no = SHIPMENT.warehouse
JOIN `ORDER` ON `ORDER`.order = SHIPMENT.order
JOIN CUSTOMER ON CUSTOMER.cust = `ORDER`.cust
WHERE CUSTOMER.Cname = \"Jose Lopez\" AND `ORDER`.ODate = \"2023-02-03\"; """
cursor.execute(cmd)
result = cursor.fetchall()
for row in result:
    w = mycol.find_one({"name": row[0]})
    imgnum = 0
    for image in w["images"]:
        file = open(w["name"] + str(imgnum)+".jpg", "xb")
        imgnum += 1
        file.write(image)
        file.close()
cursor.close()