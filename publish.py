from collections import UserString
from bson.objectid import ObjectId
from pymongo import MongoClient, collection
import pymongo
from dotenv import load_dotenv
import os
load_dotenv()

DB_PASS = os.getenv('DB_PASS')

client = pymongo.MongoClient("mongodb+srv://test:"+DB_PASS+"@cluster0.kfa3h.mongodb.net/test?retryWrites=true&w=majority")

database_name = client["test"] # Getting the database
collection_name = database_name["publish"] # Getting the collection 

# To get all the documents
def filter_data(column_name, column_value):
    all_data = collection_name.find({column_name:column_value})
    for data in all_data[:10]:
        print(data)

def year_based_filter():
    all_data = collection_name.find({"year": {"$gte": 2011}})
    for data in all_data[:10]:
        print(data)

def book_yearwise():
    all_data = collection_name.find({"year":{"$gte":2014},"type":"Book"})
    for data in all_data[:5]:
        print(data)

# Liste des publications de l’auteur « Toru Ishida » ;
def filter_author_based():
    all_data = collection_name.find({"authors": "Toru Ishida"})
    for data in all_data[:5]:
        print(data)

# Liste de tous les éditeurs (type « publisher »), distincts ;
def find_distinct(column_name):
    all_data = list(collection_name.distinct(column_name))
    print(all_data)

# Liste de tous les auteurs distincts ;
# find_distinct("authors")

# Sort the publication of « Toru Ishida » by title and by start page ;
def perform_sorting():
    all_data = list(collection_name.find({"authors":"Toru Ishida"}).sort([('title', pymongo.ASCENDING), ('pages.start', pymongo.ASCENDING)]))
    for data in all_data:
        print(data["title"])

# Count his publications ;
def countdocs():
    all_data = collection_name.count_documents({"authors":"Toru Ishida"})
    print(all_data)

def countpublications():
    all_data = collection_name.count_documents({"authors":"Toru Ishida","year":{"$gte":2011}, "$group":{"type"}})
countdocs()

# perform_sorting()
# filter_data("type", "Book")
# year_based_filter()
# book_yearwise()
# filter_author_based()
# find_distinct("publisher")
