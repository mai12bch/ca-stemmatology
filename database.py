# database file 
# import files 

# Using PyMongo

from pymongo import MongoClient 

def insert_to_db(words_dictionary): 

    words_dictionary = {str(k):str(v) for k,v in words_dictionary.items()}

    #server config
    MONGODB_HOST = 'localhost'
    MONGODB_PORT = 27017
    DBS_NAME = 'stemma'
    COLLECTION_NAME = 'words'    

    connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
    collection = connection[DBS_NAME][COLLECTION_NAME]
    words = connection[DBS_NAME][COLLECTION_NAME]

    print(collection)
    words.insert_one(words_dictionary)

    #insert_to_db(words_dictionary)
