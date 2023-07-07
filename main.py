import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['prozorro-auction']
mycol = mydb["auctions"]

mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)

print(x)