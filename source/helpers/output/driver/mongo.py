import atexit
import os

from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from helpers.output.driver import OutputDriver


class MongoOutputDriver(OutputDriver):
    name = "mongo"
    
    def __init__(self, connection_string: str, database: str, collection: str,  *args, **kwargs):
        super(MongoOutputDriver, self).__init__(*args, **kwargs)
        self.collection = collection
        self.client = MongoClient(connection_string)
        self.db = self.client[database]
        atexit.register(self.close)
        
    def put(self, output: dict):
        try:
            self.log.info(f"Sending data to collection {self.collection}")
            self.db[self.collection].insert_one(output)
            
        except DuplicateKeyError as e:
            self.log.info(f"_id is duplicate, trying update data to collection {self.collection}")
            output.pop("created_at")
            
            filter_mongo = {"_id": output.get("_id")}
            data_mongo = {
                "$set": {
                    **output
                }
            }
            self.db[self.collection].update_one(filter_mongo, data_mongo)
    
    def close(self):
        self.client.close()