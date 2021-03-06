from collections import UserString
from bson.objectid import ObjectId
from pymongo import MongoClient, collection
import pymongo
from dotenv import load_dotenv
import os
load_dotenv()

DB_PASS = os.getenv('DB_PASS')

client = pymongo.MongoClient("mongodb+srv://test:"+DB_PASS+"@cluster0.kfa3h.mongodb.net/test?retryWrites=true&w=majority")

db_name = client['test']

user = {
    "_id": "UIT",
    "email":"user2@gmail.com",
    "password": "user2"
}

# The id field must be different for each user.
user1 = {
    "_id": "UIT_1",
    "email":"user2@gmail.com",
    "password": "user2"
}

# Name of the collection
collection_name = db_name["products"]

# Insert many values at the same time
"""
collection_name.insert_many([user])
"""

# Used to insert a single data
"""
collection_name.insert_one(user1)
"""
# Returns all the data in the database
def get_all_data():
    # Retrieve data from db
    all_users = collection_name.find()
    for user in all_users:
        print(user) # Prints all the data. Its in dictonary format
        print("Username:", user["email"]) # Access each key using the dictionary access methods
        print("Password:", user["password"]) 

# Inserts new userdata into the database
def insert_user_data(product_name, product_desc, product_price ):
    # Inserting a userdata to the mongodb collection
    collection_name.insert_one({
        "_id": ObjectId(),
        "product_name": product_name,
        "product_description": product_desc,
        "product_price": product_price
    })

# To find a single user based on their email address
def find_user(username):
    # Returns a cursor object
    find_user = list(collection_name.find({"email": username}))
    if len(find_user) <=0:
        print("User not found!!")
    else:
        for user in find_user:
            print(user)

# Returns only one row. Return type is dictionary
def find_one_user(username):
    # Returns a dictionary with one row
    try:
        searched_user = collection_name.find_one({"email": username})
        print(searched_user["password"])
    except:
        print("User Not Found")

# Using regular expressions to perform querying in mongodb
def use_regex(value):
    users = collection_name.find({"email": {"$regex": "user.*"}}) # Takes all the values that begins with "user"
    for user in users:
        print(user["email"])

def remove_user(username):
    try:
        collection_name.delete_one({"email":username})
    except:
        print("User not found|Cannot perform delete")



# Find a bunch of users with the same name/email
find_one_user("Asdf")

# Removing a user
remove_user("user3@gmail.com")

# To Find a single user only
find_user("Asdf")

#Using Regex
use_regex("user")


# Inserting new user data
"""
insert_user_data(input('Enter Email Address!!\n'), input('Enter Password\n'))
"""