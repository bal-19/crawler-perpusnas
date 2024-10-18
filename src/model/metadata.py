from pydantic import BaseModel, Field, model_validator
from typing import Optional

from datetime import datetime

class MetadataModel(BaseModel):
    npp: str
    nama: str
    lembaga: str
    alamat: str
    telepon: str
    email: str
    website: str
    jenis: str
    subjenis: str
    status_perpustakaan: str
    kode_pos: str
    provinsi: str
    kabkota: str
    kecamatan: str
    kelurahan: str
    created_at: Optional[int] = Field(default_factory=lambda: int(datetime.now().timestamp() * 1000))
    updated_at: Optional[int] = Field(default_factory=lambda: int(datetime.now().timestamp() * 1000))

    @model_validator(mode="after")
    def clear_anomaly(self):
        self.nama = self.nama.strip()
        return self