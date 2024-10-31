from datetime import datetime

class mapping:
    @staticmethod
    def data(data: dict):
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
