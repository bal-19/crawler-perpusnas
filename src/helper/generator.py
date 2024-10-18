from ..model.metadata import PerpustakaanMetadataModel

from hashlib import md5
import uuid


def generate_id(data: dict) -> str:
    payload = PerpustakaanMetadataModel.model_validate(data)
    ids = f"{payload.npp}_{payload.nama}_{payload.lembaga}"
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, ids))