import pymongo
import pprint

client = pymongo.MongoClient("mongodb://localhost:27017/")

# testdb = "testdb1"

# mydb = client[testdb]

# mycol = mydb["testcollection"]

# post = {"name": "test"}

# mycol.insert_one(post)

db = "warehouse"
mydb = client[db]

# specify the collection (collection is a table in the database)
mycol = mydb["images"]

desc_inputs = ["/Users/jonathanameri/Downloads/Warehouse_desc/Husky_Vernon.pdf",
                "/Users/jonathanameri/Downloads/Warehouse_desc/Target_LA.pdf",
                "/Users/jonathanameri/Downloads/Warehouse_desc/TraderJoes_Chicago.pdf",
                "/Users/jonathanameri/Downloads/Warehouse_desc/Amazon_NY.pdf",
                "/Users/jonathanameri/Downloads/Warehouse_desc/Bobs_Phoenix.pdf",
                "/Users/jonathanameri/Downloads/Warehouse_desc/Costco_Houston.pdf",
                "/Users/jonathanameri/Downloads/Warehouse_desc/Best_Buy_Miami.pdf",
]

im_inputs = ["/Users/jonathanameri/Downloads/Warehouse_Images/Husky_Vernon.jpg",
                "/Users/jonathanameri/Downloads/Warehouse_Images/Target_LA1.jpeg",
                "/Users/jonathanameri/Downloads/Warehouse_Images/Target_LA2.jpg",
                "/Users/jonathanameri/Downloads/Warehouse_Images/Amazon_NY.jpg",
                "/Users/jonathanameri/Downloads/Warehouse_Images/Bobs_Phoenix1.jpg",
                "/Users/jonathanameri/Downloads/Warehouse_Images/Bobs_Phoenix2.jpg",
                "/Users/jonathanameri/Downloads/Warehouse_Images/Bobs_Phoenix3.jpg",
                "/Users/jonathanameri/Downloads/Warehouse_Images/Costco_Houston1.jpg",
                "/Users/jonathanameri/Downloads/Warehouse_Images/Costco_Houston2.jpg",
                "/Users/jonathanameri/Downloads/Warehouse_Images/BestBuy_Miami1.jpg",
                "/Users/jonathanameri/Downloads/Warehouse_Images/BestBuy_Miami2.jpg",
                "/Users/jonathanameri/Downloads/Warehouse_Images/BestBuy_Miami3.jpg",
                "/Users/jonathanameri/Downloads/Warehouse_Images/BestBuy_Miami4.jpg",
            ]

post0 = {
    "name": "Husky Vernon",
        "address": "123 Dog Lane, Storrs, CT",
        "description": open(desc_inputs[0], 'rb').read(),
        "images": open(im_inputs[0], 'rb').read(),
        }

post1 = {
    "name": "Target LA",
        "address": "45 Palm Road, Los Angeles, CA",
        "description": open(desc_inputs[1], 'rb').read(),
        "images": [open(im_inputs[1], 'rb').read(),
                    open(im_inputs[2], 'rb').read()],
        }

post2 = {
    "name": "TraderJoes Chicago",
        "address": "67 Snow Street, Chicago, IL",
        "description": open(desc_inputs[2], 'rb').read(),
        "images" : [],
        
        }

post3 = {
    "name": "Amazon NY",
        "address": "89 Gold Ave, New York, NY",
        "description": open(desc_inputs[3], 'rb').read(),
        "images": open(im_inputs[3], 'rb').read(),
        }


post4 = {
    "name": "Bobs Phoenix",
        "address": "101 Clay Trail, Phoenix, AZ",
        "description": open(desc_inputs[4], 'rb').read(),
        "images": [open(im_inputs[4], 'rb').read(),
                    open(im_inputs[5], 'rb').read(),
                    open(im_inputs[6], 'rb').read()],
        }

post5 = {
    "name": "Costco Houston",
        "address": "230 Ranch Drive, Houston, TX",
        "description": open(desc_inputs[5], 'rb').read(),
        "images": [open(im_inputs[7], 'rb').read(),
                    open(im_inputs[8], 'rb').read()],
        }

post6 = {
    "name": "Best Buy Miami",
        "address": "405 Sun Ridge, Miami, FL",
        "description": open(desc_inputs[6], 'rb').read(),
        "images": [open(im_inputs[9], 'rb').read(),
                    open(im_inputs[10], 'rb').read(),
                    open(im_inputs[11], 'rb').read(),
                    open(im_inputs[12], 'rb').read()],
        }

# mycol.insert_one(post0)
# mycol.insert_one(post1)
mycol.insert_one(post2)
# mycol.insert_one(post3)
# mycol.insert_one(post4)
# mycol.insert_one(post5)
# mycol.insert_one(post6)

# print(mycol.count_documents({}))


# myquery = { "name": "Costco Houston" }

# pprint.pprint(mycol.find_one(myquery))

# for x in mydoc:
#   print(x)