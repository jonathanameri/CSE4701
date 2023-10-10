import pymongo
import os

# connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = "warehouse"
mydb = client[db]

# specify the collection (collection is a table in the database)
mycol = mydb["images"]

newPFDs = "/Users/jonathanameri/Downloads/Warehouse_PDFs/"

for filename in os.listdir(newPFDs):
    if filename.endswith(".pdf"):
        fname = filename.split(".")[0].replace("_", " ")
        newPDF = open(newPFDs + filename, 'rb').read()
        mycol.update_one({"name": fname}, {"$set": {"description": newPDF}})
