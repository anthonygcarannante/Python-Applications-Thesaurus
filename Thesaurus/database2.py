import pymongo
import json


# Load in json data for dictionary of words and definitions
data = json.load(open("/Users/anthonycarannante/Desktop/Github_Repos/Udemy_Python_Apps/Real-World-Python-Applications/Thesaurus/data.json"))

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Declare the database
db = client.dictionary_db

# Declare the collection
definitions = db.definitions

test = {'Name':'Anthony',
        'Age': 27}

definitions.insert_many(test)
