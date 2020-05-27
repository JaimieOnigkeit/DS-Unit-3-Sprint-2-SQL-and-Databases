# app/mongo_queries.py

import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")

connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
print("----------------")
print("URI:", connection_uri)

client = pymongo.MongoClient(connection_uri)
print("----------------")
print("CLIENT:", type(client), client)

db = client.test_database # "test_database" or whatever you want to call it
print("----------------")
print("DB:", type(db), db)

collection = db.pokemon_test # "pokemon_test" or whatever you want to call it
print("----------------")
print("COLLECTION:", type(collection), collection)

print("----------------")
print("COLLECTIONS:")
print(db.list_collection_names())

collection.insert_one({
    "name": "Pikachu",
    "level": 30,
    "exp": 76000000000,
    "hp": 400,
})
print("DOCS:", collection.count_documents({})) #Select (count distinct id) from pokemon
print(collection.count_documents({"name": "Pikachu"})) #Select (count distinct) from pokemon where name = pikachu


#
# INSERTS
#

mewtwo = {
    "name": "Mewtwo",
    "level": 100,
    "exp": 76000000000,
    "hp": 450,
    "strength": 550,
    "intelligence": 450,
    "dexterity": 300,
    "wisdom": 575
}

mudkip = {
    "name": "Mudkip",
    "level": 30,
    "exp": 76000000000,
    "hp": 400,
}

blastoise = {
    "name": "Blastoise",
    "lvl": 70,
}

pokemon_team = [mewtwo, mudkip, blastoise]

collection.insert_many(pokemon_team)

print("DOCS:", collection.count_documents({})) #Select (count distinct id) from pokemon
print(collection.count_documents({"name": "Pikachu"})) #Select (count distinct) from pokemon where name = pikachu