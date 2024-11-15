from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from bs4 import BeautifulSoup
from datetime import datetime

import requests
import time


class Scraper:
    def __init__(self):
        self.cookies = {
            'ci_session': 'kasghvuv2v4c7f1jdl6gglbqrc843tvg',
        }
        self.headers = {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'en-US,en;q=0.9',
            'priority': 'u=1, i',
            'referer': 'https://data.perpusnas.go.id/public/direktori/perpustakaan-umum',
            'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-arch': '"x86"',
            'sec-ch-ua-bitness': '"64"',
            'sec-ch-ua-full-version': '"130.0.6723.6"',
            'sec-ch-ua-full-version-list': '"Chromium";v="130.0.6723.6", "Google Chrome";v="130.0.6723.6", "Not?A_Brand";v="99.0.0.0"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"15.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }
        self.session = requests.Session()
        self.retries = Retry(
            total=10,
            backoff_factor=0.8,
            status_forcelist=[500, 502, 503, 504]
        )
        self.adapter = HTTPAdapter(max_retries=self.retries)
        self.session.mount("http://", self.adapter)
        self.session.mount("https://", self.adapter)
    
    def get_libraries(self, url: str, start: int = 0, length: int = 10, **kwargs) -> dict:
        current_timestamp = int(datetime.now().timestamp())
        params = {
            'jenis': str(kwargs.get('jenis', '')).upper(),
            'provinsi_id': str(kwargs.get('provinsi_id', '')),
            'kabkota_id': str(kwargs.get('kabkota_id', '')),
            'kecamatan_id': str(kwargs.get('kecamatan_id', '')),
            'kelurahan_id': str(kwargs.get('kelurahan_id', '')),
            'subjenis':str(kwargs.get('subjenis', '')),
            'draw': '0',
            'columns[0][data]': 'id',
            'columns[0][name]': 'id',
            'columns[0][searchable]': 'true',
            'columns[0][orderable]': 'false',
            'columns[0][search][value]': '',
            'columns[0][search][regex]': 'false',
            'columns[1][data]': 'npp',
            'columns[1][name]': '',
            'columns[1][searchable]': 'true',
            'columns[1][orderable]': 'false',
            'columns[1][search][value]': '',
            'columns[1][search][regex]': 'false',
            'columns[2][data]': 'nama',
            'columns[2][name]': '',
            'columns[2][searchable]': 'true',
            'columns[2][orderable]': 'false',
            'columns[2][search][value]': '',
            'columns[2][search][regex]': 'false',
            'columns[3][data]': 'nama_provinsi',
            'columns[3][name]': '',
            'columns[3][searchable]': 'true',
            'columns[3][orderable]': 'false',
            'columns[3][search][value]': '',
            'columns[3][search][regex]': 'false',
            'columns[4][data]': 'nama_kabkota',
            'columns[4][name]': '',
            'columns[4][searchable]': 'true',
            'columns[4][orderable]': 'false',
            'columns[4][search][value]': '',
            'columns[4][search][regex]': 'false',
            'columns[5][data]': 'alamat',
            'columns[5][name]': '',
            'columns[5][searchable]': 'true',
            'columns[5][orderable]': 'false',
            'columns[5][search][value]': '',
            'columns[5][search][regex]': 'false',
            'columns[6][data]': 'telepon',
            'columns[6][name]': '',
            'columns[6][searchable]': 'true',
            'columns[6][orderable]': 'false',
            'columns[6][search][value]': '',
            'columns[6][search][regex]': 'false',
            'start': str(start),
            'length': str(length),
            'search[value]': '',
            'search[regex]': 'false',
            '_': str(current_timestamp),
        }
        
        response = self.session.get(url, timeout=10, params=params, cookies=self.cookies, headers=self.headers)

        if response.status_code == 200:
            print(response.url)
            result = response.json()
            return result
        
        else:
            return

    def get_type(self, url: str) -> list:
        response = self.session.get(url, timeout=10, headers=self.headers)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            type_list = list()
            
            options = soup.select("option")
            
            if options:
                for option in options:
                    type_value = option.get("value")
                    type_list.append(type_value)
                return type_list
            
            else:
                return
        else:
            return
    
    def get_region(self, url: str) -> dict:
        response = self.session.get(url, timeout=10, headers=self.headers)
        
        if response.status_code == 200:
            result = response.json()
            return result
            
        else:
            return