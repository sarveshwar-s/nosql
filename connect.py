from pymongo import MongoClient, collection
import pymongo
from credentials import DB_PASS

client = pymongo.MongoClient("mongodb+srv://test:"+DB_PASS+"@cluster0.kfa3h.mongodb.net/test?retryWrites=true&w=majority")

db_name = client['test']

user = {
    "_id": "UIT",
    "email":"user1@gmail.com",
    "password": "user1"
}

# Name of the collection
collection_name = db_name["user"]

collection_name.insert_many([user])

