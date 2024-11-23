import json
import requests
import urllib.parse

from asyncio import sleep
from datetime import datetime
from controllers.perpusnas import PerpusnasControllers
from library import generate_id


class PerpusnasGetPerpustakaan(PerpusnasControllers):

    def __init__(self, *args, **kwargs):
        super(PerpusnasGetPerpustakaan, self).__init__(*args, **kwargs)

    async def handler(self):
        list_provinsi = await self.fetch_province_data()
        for provinsi in list_provinsi:
            provinsi_id = provinsi.get("id")
            
            list_kabkota = await self.fetch_regency_data(provinsi_id)
            for kabkota in list_kabkota:
                kabkota_id = kabkota.get("id")
                
                list_kecamatan = await self.fetch_district_data(kabkota_id)
                for kecamatan in list_kecamatan:
                    kecamatan_id = kecamatan.get("id")

                    start = 0
                    while True:
                        self.log.info("Fetch data perpustakaan")
                        data = await self.fetch_libraries_data(start=start, length=20, provinsi_id=provinsi_id, kabkota_id=kabkota_id, kecamatan_id=kecamatan_id)
                        if data.get("data"):
                            for detail_data in data.get("data"):
                                if "nama_provinsi" not in detail_data or detail_data.get("nama_provinsi") is None:
                                    continue
                                
                                result = self.mapping(detail_data)
                                id_metadata = generate_id(result)
                                result["_id"] = id_metadata
                                self.log.debug(json.dumps(result))
                                self.output.put(result)
                        else:
                            break

                        if len(data.get("data")) < 20:
                            break
                        sleep(0.5)
                        start += 20

    async def fetch_libraries_data(self, start: int, length: int, **kwargs) -> dict:
        """Fetch libraries data from API"""
        url = f"{self.base_url}/public/direktori/list"
        
        libraries = await self.get_data(url, start=start, length=length, **kwargs)
        return libraries

    async def fetch_type_data(self, ) -> list[str]:
        """Fetch type data from API"""
        url = f"{self.base_url}/reference/list-dropdown/jenis-perpustakaan"
        
        types = await self.get_type(url)
        return types
    
    async def fetch_subtype_data(self, type: str) -> list[str]:
        """Fetch subtype data from API"""
        type_encode = urllib.parse.quote(type.upper())
        url = f"{self.base_url}/reference/list-dropdown/subjenis-perpustakaan/{type_encode}"
        
        subtypes = await self.get_type(url)
        return subtypes
    
    async def fetch_province_data(self, ) -> list[dict]:
        """Fetch province data from API"""
        url = f"{self.base_url}/public/kewilayahan/dati1/list-dropdown"
        
        provinces = await self.get_region(url)
        return provinces
    
    async def fetch_regency_data(self, province_id: str) -> list[dict]:
        """Fetch regency data from API"""
        url = f"{self.base_url}/public/kewilayahan/dati2/list-dropdown/{province_id}"
        
        regencies = await self.get_region(url)
        return regencies
    
    async def fetch_district_data(self, id_kabkota: str) -> list[dict]:
        """Fetch district data from API"""
        url = f"{self.base_url}/public/kewilayahan/dati3/list-dropdown/{id_kabkota}"
        
        district = await self.get_region(url)
        return district

    async def fetch_subdistrict_data(self, id_kecamatan: str) -> list[dict]:
        """Fetch subdistrict data from API"""
        url = f"{self.base_url}/public/kewilayahan/dati4/list-dropdown/{id_kecamatan}"
        
        subdistrict = await self.get_region(url)
        return subdistrict