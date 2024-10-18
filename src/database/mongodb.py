from dotenv import load_dotenv

import pymongo
import os

load_dotenv()
class Monggo:
    def __init__(self, db: str) -> None:
        self.connection_string = os.getenv("MONGO_CONNECTION_STRING")
        self.client = pymongo.MongoClient(self.connection_string)
        self.db = self.client[db]
    
    def insert(self, collection: str, data: dict) -> None:
        """Insert data to MongoDB"""
        self.db[collection].insert_one(data)
        print(f"Data successfully inserted to {collection}")

    def update(self, collection: str, filter, data: dict) -> None:
        """Update data to MongoDB"""
        self.db[collection].update_one(filter, data)
        print(f"Data successfully updated to {collection}")

    def update_many(self, collection: str, filter, data: dict) -> None:
        """Update many data to MongoDB"""
        self.db[collection].update_many(filter, data)
        print(f"Data successfully updated to {collection}")

    def delete(self, collection: str, data: dict) -> None:
        """Delete data to MongoDB"""
        self.db[collection].delete_one(data)
        print(f"Data successfully deleted to {collection}")
