class Mahasiswa:
    def __init__(self, mahasiswa_id, nama, jurusan):
        self.mahasiswa_id = mahasiswa_id
        self.nama = nama
        self.jurusan = jurusan
        self.mata_kuliah = []

    def daftar_mata_kuliah(self, mata_kuliah):
        if mata_kuliah not in self.mata_kuliah:
            self.mata_kuliah.append(mata_kuliah)
            mata_kuliah.tambah_mahasiswa(self)
            print(f"{self.nama} telah mendaftar ke mata kuliah {mata_kuliah.nama_mata_kuliah}.")

    def hapus_mata_kuliah(self, mata_kuliah):
        if mata_kuliah in self.mata_kuliah:
            self.mata_kuliah.remove(mata_kuliah)
            mata_kuliah.hapus_mahasiswa(self)
            print(f"{self.nama} telah menghapus mata kuliah {mata_kuliah.nama_mata_kuliah}.")

class MataKuliah:
    def __init__(self, mata_kuliah_id, nama_mata_kuliah, sks):
        self.mata_kuliah_id = mata_kuliah_id
        self.nama_mata_kuliah = nama_mata_kuliah
        self.sks = sks
        self.mahasiswa = []

    def tambah_mahasiswa(self, mahasiswa):
        if mahasiswa not in self.mahasiswa:
            self.mahasiswa.append(mahasiswa)

    def hapus_mahasiswa(self, mahasiswa):
        if mahasiswa in self.mahasiswa:
            self.mahasiswa.remove(mahasiswa)
# Membuat objek MataKuliah
mata_kuliah1 = MataKuliah(mata_kuliah_id=1001, nama_mata_kuliah='Pemrograman Berorientasi Objek', sks=3)

# Membuat objek Mahasiswa
mahasiswa1 = Mahasiswa(mahasiswa_id=201, nama='Rey Gavrila Naibaho', jurusan='Teknik Informatika')

# Mahasiswa mendaftar ke mata kuliah
mahasiswa1.daftar_mata_kuliah(mata_kuliah1)

# Mengecek daftar mahasiswa di mata kuliah tersebut
print(f"Mahasiswa di mata kuliah {mata_kuliah1.nama_mata_kuliah}: {[mahasiswa.nama for mahasiswa in mata_kuliah1.mahasiswa]}")

# Mahasiswa menghapus mata kuliah dari daftar mata kuliah yang diambil
mahasiswa1.hapus_mata_kuliah(mata_kuliah1)

# Mengecek daftar mahasiswa setelah dihapus dari mata kuliah
print(f"Mahasiswa di mata kuliah {mata_kuliah1.nama_mata_kuliah} setelah dihapus: {[mahasiswa.nama for mahasiswa in mata_kuliah1.mahasiswa]}")
