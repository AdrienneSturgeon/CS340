from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelterCrud(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password, host, port, database, collection):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = username
        PASS = password
        HOST = host
        PORT = port
        DB = database
        COL = collection
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        try:
            result = self.collection.insert_one(data)
            return True if result.inserted_id else False
        except Exception as e:
            print(f"Document insert failed: {e}")
            return False

# Create method to implement the R in CRUD.
    def read(self, query):
        try:
            cursor = self.collection.find(query)
            return list(cursor) 
        except Exception as e:
            print(f"Document query failed: {e}")
            return []
        
# This is my Update method which represents the U in CRUD
    def update(self, query, data_new):
    #This lets me update documents in MongoDB
      try:
        outcome = self.collection.update_many(query, {'$set': data_new})
        return outcome.modified_count
      except Exception as error:
        print(f"The update failed because: {error}")
        return 0
    
# This is my Delte method which represents the D in CRUD
    def delete(self, query):
    #This lets me delete within documents in MongoDB
      try:
        outcome = self.collection.delete_many(query)
        return outcome.deleted_count
      except Exception as error:
        print(f"The delete failed because: {error}")
        return 0
