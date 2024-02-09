from pymongo import MongoClient
from pprint import pprint
from bson.objectid import ObjectId


# Connect to the MongoDB cluster
client = MongoClient("mongodb+srv://pr1735h:vPvcoOjrKHF6r7Em@cluster0.zu2wfsw.mongodb.net/")
# To connect directly to the c9w4 database:
# client = MongoClient("mongodb+srv://pr1735h:vPvcoOjrKHF6r7Em@cluster0.zu2wfsw.mongodb.net/c9w4")

# Specify the database and collection names
db_name = "c9w4"
collection_name = "course"
collection_name2 = "lesson"

# Get the collection object
mongo_db = client[db_name]
mongo_coll = mongo_db[collection_name]
mongo_coll2 = mongo_db[collection_name2]
# Retrieve all documents using find()
all_docs_cursor = mongo_coll.find()

# Convert the cursor to a list (if needed)
all_docs_list = list(all_docs_cursor)

# Pretty print the documents
pprint(all_docs_list)

# Retrieve a single document using find_one()
docs = mongo_coll.find_one()

pprint(docs)

# METHOD 2:
print("\nAll documents\n")
#use the find method to retrieve all documents from the members collection
docs2 = mongo_coll2.find()
for aDoc in docs2:
    pprint(aDoc)

# METHOD 3:
dbMongoClient = client["c9w4"]['lesson']
coll = dbMongoClient.find_one({'CourseID':5})
pprint(coll)


# ADD DOCUMENTS:
# print("\Insert Single Document\n")
# addDoc = dbMongoClient.insert_one({"CourseID": 29,"MemberID": 35})
# print(addDoc.inserted_id)

# ADD MULTIPLE DOCUMENTS:
# print("\Insert Multiple Documents\n")
# documents = [
#     {"CourseID": 49,"MemberID": 3},
#     {"CourseID": 72,"MemberID": 5},
#     {"CourseID": 12,"MemberID": 21},
#     {"CourseID": 21,"MemberID": 12},
#     {"CourseID": 27,"MemberID": 35},
#     {"CourseID": 29,"MemberID": 36}
# ]

# addDocs = dbMongoClient.insert_many(documents)
# print(addDocs.inserted_ids)

# UPDATE DOCUMENTS:
# print("Update a document\n")
# updateDoc = dbMongoClient.update_one({"CourseID": 72}, {'$set':{"MemberID": 25}})
# print(updateDoc.modified_count)

# UPDATE MULTIPLE DOCUMENTS:
# print("\nUpdate Multiple documents\n")
# updateDocs = dbMongoClient.update_many({"CourseID": 29}, {'$set':{"CourseID": 2111}})
# print(f"The number of updated documents: {updateDocs.modified_count}")

# DELETE DOCUMENTS:
# Create an ObjectID instance
# document_id = ObjectId('65c4a80f9cc973d20af4e939')

# print("\nDelete single document\n")
# deleteOne = dbMongoClient.delete_one({"_id": document_id})
# print(f"Deleted {deleteOne.deleted_count} document")

# DELETE MULTIPLE DOCUMENTS:
# print("\nDelete Multiple documents\n")
# deletemany = dbMongoClient.delete_many({'CourseID': 2111})
# print(f"Deleted {deletemany.deleted_count} document")

# client.close() This method ends the connection