import datetime   # This will be needed later
import os

from pymongo import MongoClient

# Load config from a .env file:
MONGODB_URI = 'mongodb+srv://anirmal_admin:Databases123@cluster0.5oiydpy.mongodb.net/'

# Connect to your MongoDB cluster:
client = MongoClient(MONGODB_URI)

# List all the databases in the cluster:
for db_info in client.list_database_names():
    db = client[db_info]
    collections = db.list_collection_names()
    for collection in collections:
        print("Collection: ", collection)
    print("db: ", db.name)