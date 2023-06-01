class Mahasiswa:  # deklarasi kelas dengan nama "Mahasiswa".
    def __init__(self, nama, nim, jurusan):  # metode khusus yang disebut sebagai konstruktor. Metode ini akan dipanggil saat objek kelas Mahasiswa dibuat.
        self.nama = nama  # atribut nama dari objek Mahasiswa yang akan disimpan dalam instance kelas.
        self.nim = nim  # atribut nim dari objek Mahasiswa yang akan disimpan dalam instance kelas.
        self.jurusan = jurusan  # atribut jurusan dari objek Mahasiswa yang akan disimpan dalam instance kelas.

    def tampilkan_info(self, ):  # metode yang digunakan untuk menampilkan informasi mahasiswa.
        print("Nama:", self.nama)  # perintah cetak yang menampilkan informasi nama.
        print("NIM:", self.nim)  # perintah cetak yang menampilkan informasi nim.
        print(
            "Jurusan:", self.jurusan.NamaJurusan
        )  # perintah cetak yang menampilkan informasi jurusan.


class Jurusan:  # deklarasi kelas dengan nama "Jurusan".
    def __init__(self, nama_jurusan):  # konstruktor kelas Jurusan. Metode ini akan dipanggil saat objek kelas Jurusan dibuat.
        self.NamaJurusan = (nama_jurusan ) #  atribut dari objek Jurusan yang menyimpan nama jurusan.
        self.DaftarMahasiswa = ([])  # atribut dari objek Jurusan yang berfungsi untuk menyimpan daftar mahasiswa yang terdaftar dalam jurusan tersebut.

    def tambah_mahasiswa(self, mahasiswa):  # metode yang digunakan untuk menambahkan objek mahasiswa ke dalam daftar mahasiswa di jurusan.
        self.DaftarMahasiswa.append( mahasiswa)  # menambahkan objek mahasiswa ke daftar mahasiswa di jurusan.

    def tampilkan_daftar_mahasiswa(self,):  # metode yang digunakan untuk menampilkan daftar mahasiswa dalam jurusan.
        print("Daftar Mahasiswa di Jurusan", self.NamaJurusan + ":")  # mencetak judul daftar mahasiswa.
        for (mahasiswa) in (self.DaftarMahasiswa):  #  loop for yang digunakan untuk mencetak informasi setiap mahasiswa dalam daftar mahasiswa jurusan.
            print("- Nama:", mahasiswa.nama)  # mencetak informasi nama mahasiswa.
            print("- NIM:", mahasiswa.nim)  # mencetak informasi NIM mahasiswa.


class Universitas:  # deklarasi kelas dengan nama "Universitas".
    def __init__(self, nama_universitas):  # konstruktor kelas Universitas. Metode ini akan dipanggil saat objek kelas Universitas dibuat.
        self.NamaUniversitas = nama_universitas  # atribut dari objek Universitas yang menyimpan nama universitas.
        self.DaftarJurusan = []  # atribut dari objek Universitas yang berfungsi untuk menyimpan daftar jurusan di universitas tersebut.

    def tambah_jurusan(self, jurusan):  # metode yang digunakan untuk menambahkan objek jurusan ke dalam daftar jurusan di universitas.
        self.DaftarJurusan.append(jurusan)  # menambahkan objek jurusan ke daftar jurusan di universitas.

    def tampilkan_daftar_jurusan(self):  # metode yang digunakan untuk menampilkan daftar jurusan dalam universitas.
        print("Daftar Jurusan di Universitas", self.NamaUniversitas + ":")  # mencetak judul daftar jurusan.
        for jurusan in self.DaftarJurusan:  #  loop for yang digunakan untuk mencetak informasi setiap jurusan dalam daftar jurusan universitas.
            print("- Nama Jurusan:", jurusan.NamaJurusan)  # mencetak informasi nama jurusan.


universitas_xyz = Universitas("XYZ University") # Membuat objek universitas_xyz dari kelas Universitas dengan nama "XYZ University".

jurusan_ti = Jurusan("Teknik Informatika") # Membuat objek jurusan_ti dari kelas Jurusan dengan nama jurusan "Teknik Informatika".
universitas_xyz.tambah_jurusan(jurusan_ti) # Menambahkan objek jurusan_ti ke dalam daftar jurusan universitas_xyz menggunakan metode tambah_jurusan.

mahasiswa1 = Mahasiswa("Daffa Fadhil Apriza", "G1A022067", jurusan_ti) # Membuat objek mahasiswa1 dari kelas Mahasiswa dengan nama "Daffa Fadhil Apriza", NIM "G1A022067", dan jurusan jurusan_ti.
jurusan_ti.tambah_mahasiswa(mahasiswa1) # Menambahkan objek mahasiswa1 ke dalam daftar mahasiswa di jurusan_ti menggunakan metode tambah_mahasiswa.

universitas_xyz.tampilkan_daftar_jurusan() # Menampilkan daftar jurusan dalam universitas_xyz menggunakan metode tampilkan_daftar_jurusan.

jurusan_ti.tampilkan_daftar_mahasiswa() # Menampilkan daftar mahasiswa dalam jurusan_ti menggunakan metode tampilkan_daftar_mahasiswa.
