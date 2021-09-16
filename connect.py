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
collection_name = db_name["user"]

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
def insert_user_data(username, password):
    # Inserting a userdata to the mongodb collection
    collection_name.insert_one({
        "_id": ObjectId(),
        "email": username,
        "password": password
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


def remove_column_regex(column_name):
    try:
        collection_name.delete_many({column_name: {"$exists": True}})
    except:
        print("Column does not exists| Cannot perform delete")

# To remove a particular column and retain the document
def remove_column_unset(column_name):
    try:
        collection_name.update_many({},{"$unset": {column_name: ""} })
    except:
        print("Column does not exists| Cannot do unset")
# Updates a single column based on the id of the column. 
# Before performing an update we must always perform a find operation. 
def update_column(column_id,column_name, new_value):
    try:
        collection_name.update_one({"_id": column_id},{"$set":{column_name: new_value}})
        print("column updated.")
    except:
        print("Column does not exists or cannot be updated!")
def another_update_method():
    users = list(collection_name.find({}))
    if len(users) <= 0:
        print("No users found !")
    else:
        for index, user in enumerate(users):
            print(str(index) + " " + str(user.get("email")))
        delete_number = int(input("Which user to delete from the database?"))
        new_name = input("Enter an alternative email id")
        for index, user in enumerate(users):
            if index == delete_number:
                id = user.get("_id")
        print(id)
        collection_name.update_one({"_id":id},{"$set": {"email": new_name}})

another_update_method()

update_column(ObjectId("6143334cea4b234d07d17628"), "email", "user4@gmail.com")

remove_column_unset("todo")

# Find a bunch of users with the same name/email
find_one_user("Asdf")

# Removing a user
remove_user("user3@gmail.com")

# Removing the entries that contain the column todo 
# remove_column_regex("todo")

# To Find a single user only
find_user("Asdf")

#Using Regex
use_regex("user")


# Inserting new user data
"""
insert_user_data(input('Enter Email Address!!\n'), input('Enter Password\n'))
"""