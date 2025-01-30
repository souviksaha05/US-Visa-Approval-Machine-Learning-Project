import sys

from us_visa.exception import USvisaException
from us_visa.logger import logging

import os
from us_visa.constants import DATABASE_NAME, MONGODB_URL_KEY
import pymongo
import certifi

ca = certifi.where()

class MongoDBClient:
    """
    Class Name :   export_data_into_feature_store
    Description :   This method exports the dataframe from mongodb feature store as dataframe 
    
    Output      :   connection to mongodb database
    On Failure  :   raises an exception
    """
    client = None

    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                if mongo_db_url is None:
                    raise Exception(f"Environment key: {MONGODB_URL_KEY} is not set.")
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info("MongoDB connection succesfull")
        except Exception as e:
            raise USvisaException(e,sys)

'''
import sys
from us_visa.exception import USvisaException
from us_visa.logger import logging
import os
from us_visa.constants import DATABASE_NAME, MONGODB_URL_KEY
import pymongo
import certifi
from urllib.parse import quote_plus

ca = certifi.where()

class MongoDBClient:
    """
    Class Name :   MongoDBClient
    Description :   This class connects to the MongoDB database.

    Output      :   Connection to the MongoDB database.
    On Failure  :   Raises an exception.
    """
    client = None

    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                if mongo_db_url is None:
                    raise Exception(f"Environment key: {MONGODB_URL_KEY} is not set.")

                # Parse the MongoDB URL to ensure special characters are escaped
                if "mongodb://" in mongo_db_url or "mongodb+srv://" in mongo_db_url:
                    # Extract username and password from the URL if present
                    if "@" in mongo_db_url:
                        parts = mongo_db_url.split("@")
                        credentials, host_part = parts[0], parts[1]
                        if "//" in credentials:
                            credentials = credentials.split("//")[1]
                        username, password = credentials.split(":")
                        username = quote_plus(username)
                        password = quote_plus(password)
                        mongo_db_url = f"mongodb+srv://{username}:{password}@{host_part}"
                
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info("MongoDB connection successful")
            
        except Exception as e:
            raise USvisaException(e, sys)
'''