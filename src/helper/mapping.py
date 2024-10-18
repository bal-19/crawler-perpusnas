from datetime import datetime

class mapping:
    @staticmethod
    def data(data: dict):
        npp = data.get("npp") if data.get("npp") else "-"
        nama = data.get("nama") if data.get("nama") else "-"
        lembaga_induk = data.get("lembaga_induk") if data.get("lembaga_induk") else "-"
        alamat = data.get("alamat") if data.get("alamat") else "-"
        telepon = data.get("telepon") if data.get("telepon") else "-"
        email = data.get("email") if data.get("email") else "-"
        website = data.get("website") if data.get("website") else "-"
        jenis = data.get("jenis") if data.get("jenis").capitalize() else "-"
        sub_jenis = data.get("subjenis") if data.get("subjenis") else "-"
        status_perpus = data.get("status_perpus").capitalize() if data.get("status_perpus") else "-"
        kode_pos = data.get("kode_pos") if data.get("kode_pos") else "-"
        provinsi = data.get("nama_provinsi") if data.get("nama_provinsi") else "-"
        kabkota = data.get("nama_kabkota") if data.get("nama_kabkota") else "-"
        kecamatan = data.get('nama_kecamatan') if data.get("nama_kecamatan") else "-"
        kelurahan = data.get("nama_kelurahan").capitalize() if data.get("nama_kelurahan") else "-"
        
        return dict(
            npp=npp,
            nama=nama,
            lembaga=lembaga_induk,
            alamat=alamat,
            telepon=telepon,
            email=email,
            website=website,
            jenis=jenis,
            subjenis=sub_jenis,
            status_perpustakaan=status_perpus,
            kode_pos=kode_pos,
            provinsi=provinsi,
            kabkota=kabkota,
            kecamatan=kecamatan,
            kelurahan=kelurahan,
            created_at=int(datetime.now().timestamp() * 1000),
            updated_at=int(datetime.now().timestamp() * 1000)
        )
