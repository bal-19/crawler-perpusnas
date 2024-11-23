from model.metadata import PerpustakaanMetadataModel
from hashlib import md5

import uuid

def generate_id(data: dict) -> str:
    payload = PerpustakaanMetadataModel.model_validate(data)
    ids = f"{payload.provinsi}_{payload.kabkota}_{payload.kecamatan}_{payload.kelurahan}_{payload.nama}"
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, ids))