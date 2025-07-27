from pymongo import MongoClient
from api.utils.core import settings

def get_mongo_client():
    """
    Get a MongoDB client instance.
    """
    try:
        client = MongoClient(settings.MONGO_URI)
        return client
    except Exception as e:
        raise Exception(f"Could not connect to MongoDB: {e}")
    
def insert_document(collection_name, document):
    """
    Insert a document into a specified MongoDB collection.
    """
    client = get_mongo_client()
    db = client[settings.MONGO_DB_NAME]
    collection = db[collection_name]
    
    try:
        result = collection.insert_one(document)
        return str(result.inserted_id)
    except Exception as e:
        raise Exception(f"Could not insert document: {e}")

def find_documents(collection_name, query):
    """
    Find documents in a specified MongoDB collection based on a query.
    """
    
    try:
        client = get_mongo_client()
        db = client[settings.MONGO_DB_NAME]
        collection = db[collection_name]
        documents = list(collection.find(query))
        return documents
    except Exception as e:
        raise Exception(f"Could not find documents: {e}")
    
def update_document(collection_name, query, update):
    """
    Update documents in a specified MongoDB collection based on a query.
    """
    client = get_mongo_client()
    db = client[settings.MONGO_DB_NAME]
    collection = db[collection_name]
    
    try:
        result = collection.update_many(query, update)
        return result.modified_count
    except Exception as e:
        raise Exception(f"Could not update documents: {e}")
    