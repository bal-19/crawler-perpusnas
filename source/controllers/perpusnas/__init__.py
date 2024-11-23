from requests.adapters import HTTPAdapter
from datetime import datetime
from urllib3.util.retry import Retry
from controllers import Controllers
from helpers.html_parser import HtmlParser

import requests


class PerpusnasControllers(Controllers):

    def __init__(self, *args, **kwargs):
        super(PerpusnasControllers, self).__init__(*args, **kwargs)
        self.base_url = "https://data.perpusnas.go.id"
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
        
        self.parser = HtmlParser()
    
    def mapping(self, data: dict):
        npp = data.get("npp") if data.get("npp") else None
        npp_lama = data.get("npp_lama") if data.get("npp_lama") else None
        nama = data.get("nama") if data.get("nama") else None
        lembaga_induk = data.get("lembaga_induk") if data.get("lembaga_induk") else None
        alamat = data.get("alamat") if data.get("alamat") else None
        telepon = data.get("telepon") if data.get("telepon") else None
        email = data.get("email") if data.get("email") else None
        website = data.get("website") if data.get("website") else None
        jenis = data.get("jenis") if data.get("jenis").capitalize() else None
        sub_jenis = data.get("subjenis") if data.get("subjenis") else None
        status_perpus = data.get("status_perpus").capitalize() if data.get("status_perpus") else None
        kode_pos = data.get("kode_pos") if data.get("kode_pos") else None
        provinsi = data.get("nama_provinsi") if data.get("nama_provinsi") else None
        kabkota = data.get("nama_kabkota") if data.get("nama_kabkota") else None
        kecamatan = data.get('nama_kecamatan') if data.get("nama_kecamatan") else None
        kelurahan = data.get("nama_kelurahan").capitalize() if data.get("nama_kelurahan") else None
        
        return dict(
            npp=npp,
            npp_lama=npp_lama,
            nama=nama,
            lembaga=lembaga_induk,
            jenis=jenis,
            subjenis=sub_jenis,
            status=status_perpus,
            alamat=alamat,
            telepon=telepon,
            email=email,
            website=website,
            kode_pos=kode_pos,
            kelurahan=kelurahan,
            kecamatan=kecamatan,
            kabkota=kabkota,
            provinsi=provinsi,
            created_at=int(datetime.now().timestamp() * 1000),
            updated_at=int(datetime.now().timestamp() * 1000)
        )
    
    async def get_data(self, url: str, start: int = 0, length: int = 10, **kwargs) -> dict | None:
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
            self.log.debug(response.url)
            result = response.json()
            return result
        
        else:
            return None
    
    async def get_type(self, url: str) -> list:
        response = self.session.get(url, timeout=10, headers=self.headers)
        
        if response.status_code == 200:
            type_list = list()
            
            options = self.parser.bs4_parser(response.text, "option")
            if options:
                for option in options:
                    type_value = option.get("value")
                    type_list.append(type_value)
                return type_list
            
            else:
                return
        else:
            return
    
    async def get_region(self, url: str) -> dict:
        response = self.session.get(url, timeout=10, headers=self.headers)
        
        if response.status_code == 200:
            result = response.json()
            return result
            
        else:
            return