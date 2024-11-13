from ..database.mongodb import Monggo
from ..helper.generator import generate_id
from ..helper.mapping import mapping
from ..helper.fetch import fetch

from pymongo.errors import DuplicateKeyError
from time import sleep      
import json

class Perpusnas:
    def __init__(self) -> None:
        self.mongo = Monggo("perpustakaan")
    
    def run(self):
        list_provinsi = fetch.fetch_province_data()
        for provinsi in list_provinsi:
            provinsi_id = provinsi.get("id")
            
            list_kabkota = fetch.fetch_regency_data(provinsi_id)
            for kabkota in list_kabkota:
                kabkota_id = kabkota.get("id")
                
                list_kecamatan = fetch.fetch_district_data(kabkota_id)
                for kecamatan in list_kecamatan:
                    kecamatan_id = kecamatan.get("id")

                    start = 0
                    while True:
                        data = fetch.fetch_libraries_data(start=start, length=20, provinsi_id=provinsi_id, kabkota_id=kabkota_id, kecamatan_id=kecamatan_id)
                        if data.get("data"):
                            for detail_data in data.get("data"):
                                if "nama_provinsi" not in detail_data or detail_data.get("nama_provinsi") is None:
                                    continue
                                
                                result = mapping.data(detail_data)
                                id_metadata = generate_id(result)
                                result["_id"] = id_metadata
                                print(result)
                                
                                try:
                                    self.mongo.insert(result, collection="data")
                                except DuplicateKeyError as e:
                                    result.pop("created_at")
                                    
                                    filter_mongo = {"_id": id_metadata}
                                    data_mongo = {
                                        "$set": {
                                            **result
                                        }
                                    }

                                    self.mongo.update(data_mongo, collection="data", filter=filter_mongo)
                        else:
                            break

                        if len(data.get("data")) < 20:
                            break
                        sleep(2)
                        start += 20