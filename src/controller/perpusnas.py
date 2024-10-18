from ..database.mongodb import Monggo
from ..helper.generator import generate_id
from ..helper.mapping import mapping
from ..helper.fetch import fetch

from pymongo.errors import DuplicateKeyError
import json

class Perpusnas:
    def __init__(self) -> None:
        self.mongo = Monggo("perpustakaan")
    
    def run(self):
        start = 0
        while True:
            res = fetch.fetch_libraries_data(start=start, length=100)
            if res.get("data") is not []:
                for data in res.get("data"):
                    result = mapping.data(data)
                    metadata_id = generate_id(result)
                    result["_id"] = metadata_id
                    try:
                        self.mongo.insert("data", data=result)
                    except DuplicateKeyError:
                        self.mongo.update("data", {"_id": metadata_id}, {"$set": result})
            else:
                break
            start += 100
