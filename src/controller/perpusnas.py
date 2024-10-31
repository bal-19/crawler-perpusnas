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
        list_provinsi = fetch.fetch_province_data()
        for provinsi in list_provinsi:
            provinsi_id = provinsi.get("id")
            
            list_kabkota = fetch.fetch_regency_data(provinsi_id)
            for kabkota in list_kabkota:
                kabkota_id = kabkota.get("id")
                
                list_kecamatan = fetch.fetch_district_data(kabkota_id)
                for kecamatan in list_kecamatan:
                    kecamatan_id = kecamatan.get("id")

                    list_kelurahan = fetch.fetch_subdistrict_data(kecamatan_id)
                    for kelurahan in list_kelurahan:
                        kelurahan_id = kelurahan.get("id")
                        
                        list_kategori = fetch.fetch_type_data()
                        for kategori in list_kategori:
                            list_subkategori = fetch.fetch_subtype_data(kategori)
                            
                            for subkategori in list_subkategori:
                                start = 0
                                while True:
                                    data = fetch.fetch_libraries_data(start=start, length=10, jenis=kategori, provinsi_id=provinsi_id, kabkota_id=kabkota_id, kecamatan_id=kecamatan_id, kelurahan_id=kelurahan_id, subjenis=subkategori)
                                    
                                    if data.get("data"):
                                        for detail_data in data.get("data"):
                                            result = mapping.data(detail_data)
                                    else:
                                        break