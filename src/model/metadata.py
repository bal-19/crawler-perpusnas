from pydantic import BaseModel, Field, model_validator
from typing import Optional

from datetime import datetime

class PerpustakaanMetadataModel(BaseModel):
    npp: str | None
    npp_lama: str | None
    nama: str
    lembaga: str | None
    jenis: str
    subjenis: str
    status: str | None
    alamat: str | None
    telepon: str | None
    email: str | None
    website: str | None
    kode_pos: str | None
    kelurahan: str | None
    kecamatan: str
    kabkota: str
    provinsi: str
    created_at: Optional[int] = Field(default_factory=lambda: int(datetime.now().timestamp() * 1000))
    updated_at: Optional[int] = Field(default_factory=lambda: int(datetime.now().timestamp() * 1000))

    @model_validator(mode="after")
    def clear_anomaly(self):
        self.nama = self.nama.strip()
        return self