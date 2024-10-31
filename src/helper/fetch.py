from .scraper import Scraper

from dotenv import load_dotenv

import urllib.parse
import os


load_dotenv()
BASE_URL = "https://data.perpusnas.go.id"

class fetch:
    
    @staticmethod
    def fetch_libraries_data(start: int, length: int, **kwargs) -> dict:
        """Fetch libraries data from API"""
        url = f"{BASE_URL}/public/direktori/list"
        
        libraries = Scraper().get_libraries(url, start=start, length=length, **kwargs)
        return libraries

    @staticmethod
    def fetch_type_data() -> list[str]:
        """Fetch type data from API"""
        url = f"{BASE_URL}/reference/list-dropdown/jenis-perpustakaan"
        
        types = Scraper().get_type(url)
        return types
    
    @staticmethod
    def fetch_subtype_data(type: str) -> list[str]:
        """Fetch subtype data from API"""
        type_encode = urllib.parse.quote(type.upper())
        url = f"{BASE_URL}/reference/list-dropdown/subjenis-perpustakaan/{type_encode}"
        
        subtypes = Scraper().get_type(url)
        return subtypes
    
    @staticmethod
    def fetch_province_data() -> list[dict]:
        """Fetch province data from API"""
        url = f"{BASE_URL}/public/kewilayahan/dati1/list-dropdown"
        
        provinces = Scraper().get_region(url)
        return provinces
    
    @staticmethod
    def fetch_regency_data(province_id: str) -> list[dict]:
        """Fetch regency data from API"""
        url = f"{BASE_URL}/public/kewilayahan/dati2/list-dropdown/{province_id}"
        
        regencies = Scraper().get_region(url)
        return regencies
    
    @staticmethod
    def fetch_district_data(id_kabkota: str) -> list[dict]:
        """Fetch district data from API"""
        url = f"{BASE_URL}/public/kewilayahan/dati3/list-dropdown/{id_kabkota}"
        
        district = Scraper().scrape_region(url)
        return district

    def fetch_subdistrict_data(id_kecamatan: str) -> list[dict]:
        """Fetch subdistrict data from API"""
        url = f"{BASE_URL}/public/kewilayahan/dati4/list-dropdown/{id_kecamatan}"
        
        subdistrict = Scraper().scrape_region(url)
        return subdistrict
