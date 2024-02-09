from pymongo import MongoClient # import thr mongoclient from the pymongo library
from pprint import pprint
# variable and passed your mongdb connection string MongoClient(mongodbsrv//username;password@cluser.mongodb.net)
" variable= MongoClient('mongodb+srv://<username>:<password>@cluster0.cuzzc.mongodb.net/')"
# client store the connection to mongo db
client = MongoClient("mongodb+srv://<username>:<password>@cluster0.cuzzc.mongodb.net/")

# method 1
# pass the connection to mongodb from the variable "client" with the sample training db "
# db = client['sample_training'] 
# passing the collection "companies " to the varible  myCollection
# myCollection = db["companies"]
# myDoc = myCollection.find_one() # accessing one document 
# pprint(myDoc) #print one document
# print(myDoc)

# method 2 
# pass the connection to mongodb from the variable "client" with the sample training db and the collection "grades" "
db1 = client['sample_training'] ['grades']

for myQuery1 in db1.find():
    pprint(myQuery1)

# query2 = db1.find_one({"class_id ": 82.0})
# pprint(query2)


# db1 = client["sample_training"]["grades"]
# myQuery = db1.find_one({"class_id": 350})
# pprint(myQuery)
# myQuery1 = {"class_id ":350}
# pprint(myQuery1.find({"class_id ":350}))
# connect to a different database 
# db2 = client['sample_airbnb']['listingsAndReviews']

# mycol.drop()
# query = {"member_id": 3}
# query = {"Adress.city": {"$eq":"London"}}
# query = {"Adress.pcode": {"$eq":"DB1 2CC"}}
# # query = {"firstname": {"$eq":"Anna"}}
# mydoc = mycol.find_one(query)
# mydoc = mycol.delete_one()
# mydoc = mycol.update_one()

