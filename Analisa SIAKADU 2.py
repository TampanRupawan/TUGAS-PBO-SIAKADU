class Mahasiswa:
    def __init__(self, nama, npm, jurusan):
        self.nama = nama
        self.npm = npm
        self.jurusan = jurusan

    def lihat_pengumuman(self, pengumuman):
        print(f"Pengumuman untuk {self.nama}: {pengumuman}")

class Dosen:
    def __init__(self, nama, nip, departemen):
        self.nama = nama
        self.nip = nip
        self.departemen = departemen

    def buat_pengumuman(self, pengumuman):
        print(f"Dosen {self.nama} membuat pengumuman: {pengumuman}")

class SIAKADU:
    def __init__(self):
        self.mahasiswa_list = []
        self.dosen_list = []

    def tambah_mahasiswa(self, mahasiswa):
        self.mahasiswa_list.append(mahasiswa)
        print(f"Mahasiswa {mahasiswa.nama} telah ditambahkan ke sistem")

    def tambah_dosen(self, dosen):
        self.dosen_list.append(dosen)
        print(f"Dosen {dosen.nama} telah ditambahkan ke sistem")

    def umumkan_pengumuman(self, pengumuman):
        for mahasiswa in self.mahasiswa_list:
            mahasiswa.lihat_pengumuman(pengumuman)
        for dosen in self.dosen_list:
            dosen.buat_pengumuman(pengumuman)

# Contoh penggunaan
if __name__ == "__main__":
    # Membuat objek SIAKADU
    siakadu = SIAKADU()

    # Membuat dan menambahkan mahasiswa
    mahasiswa1 = Mahasiswa("Aryudha", "221506055", "Teknik Informatika")
    siakadu.tambah_mahasiswa(mahasiswa1)

    # Membuat dan menambahkan dosen
    dosen1 = Dosen("Pak Puput", "87654321", "Teknik Informatika")
    siakadu.tambah_dosen(dosen1)

    # SIAKADU membuat pengumuman
    siakadu.umumkan_pengumuman("Ujian Tengah Semester akan dimulai minggu depan")
