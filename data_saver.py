from pymongo import MongoClient

# import dotenv
config["host"] = "mongodb://localhost:27017/"
config["database_name"] =
config["collection_name"] =

client = MongoClient()

# Or use the MongoDB URI format:
# client = MongoClient('localhost', 27017)
# client = MongoClient("mongodb://localhost:27017/")
print(dir(client))
print(client.list_databases())
print(client.list_database_names())


db = client[]
# collections = db.show_collections()
# print(collections)

# action_sequences = db[config["collection_name"]].find()
# for problem in problems:
#     print(problem)

def save_data():
    # - header (i.e. what kind of action is added in sequence)
    # - content of this action
    # - timestamp
    # - session ID
    try:
        
        return True #?
    except e:
        return e