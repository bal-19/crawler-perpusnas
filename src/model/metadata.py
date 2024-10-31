from pydantic import BaseModel, Field, model_validator
from typing import Optional

from datetime import datetime

class PerpustakaanMetadataModel(BaseModel):
    npp: str
    npp_lama: str
    nama: str
    lembaga: str
    jenis: str
    subjenis: str
    status: str
    alamat: str
    telepon: str
    email: str
    website: str
    kode_pos: str
    kelurahan: str
    kecamatan: str
    kabkota: str
    provinsi: str
    created_at: Optional[int] = Field(default_factory=lambda: int(datetime.now().timestamp() * 1000))
    updated_at: Optional[int] = Field(default_factory=lambda: int(datetime.now().timestamp() * 1000))

    @model_validator(mode="after")
    def clear_anomaly(self):
        self.nama = self.nama.strip()
        return self