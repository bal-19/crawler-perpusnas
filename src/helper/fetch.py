from .scraper import Scraper

from dotenv import load_dotenv

import urllib.parse
import os


load_dotenv()
BASE_URL = os.getenv("URL_SCRAPING")

class fetch:
    
    @staticmethod
    def fetch_libraries_data(start: int, length: int) -> dict:
        """Fetch libraries data from API"""
        url = f"{BASE_URL}/public/direktori/list"
        
        libraries = Scraper().get_libraries(url, start=start, length=length)
        return libraries

    @staticmethod
    def fetch_type_data() -> list:
        """Fetch type data from API"""
        url = f"{BASE_URL}/reference/list-dropdown/jenis-perpustakaan"
        
        types = Scraper().get_type(url)
        return types
    
    @staticmethod
    def fetch_subtype_data(type: str) -> list:
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
    
    
