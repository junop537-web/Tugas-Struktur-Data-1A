from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListMahasiswa:
    def __init__(self):
        self.head = None

    def tambah_data(self, data):
        node_baru = Node(data)
        if not self.head:
            self.head = node_baru
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node_baru

    def tampilkan(self):
        temp = self.head
        hasil = []
        while temp:
            hasil.append(str(temp.data))
            temp = temp.next
        print(" -> ".join(hasil))


class StackUndo:
    def __init__(self):
        self.stack = []

    def lakukan_aksi(self, aksi):
        print(f"Melakukan aksi: {aksi}")
        self.stack.append(aksi)

    def undo(self):
        if not self.stack:
            print("Tidak ada aksi untuk di-undo.")
            return None
        aksi_terakhir = self.stack.pop()
        print(f"Mengurungkan (Undo) aksi: {aksi_terakhir}")
        return aksi_terakhir


class AntreanPengolahan:
    def __init__(self):
        self.queue = deque()

    def tambah_antrean(self, tugas):
        print(f"Tugas ditambahkan ke antrean: {tugas}")
        self.queue.append(tugas)

    def proses_antrean(self):
        if not self.queue:
            print("Antrean kosong.")
            return None
        tugas_diproses = self.queue.popleft()
        print(f"Memproses antrean: {tugas_diproses}")
        return tugas_diproses


class SystemMahasiswaHash:
    def __init__(self):
        self.data_mahasiswa = {}  

    def tambah_mahasiswa(self, nim, nama, jurusan):
        self.data_mahasiswa[nim] = {"Nama": nama, "Jurusan": jurusan}

    def cari_by_nim(self, nim):
        mahasiswa = self.data_mahasiswa.get(nim)
        if mahasiswa:
            print(f"Data Ditemukan (Key {nim}): {mahasiswa}")
        else:
            print(f"Data dengan NIM {nim} tidak ditemukan.")


if __name__ == "__main__":
    print("=== 1. PENYIMPANAN DATA BERURUTAN (Linked List) ===")
    list_mhs = LinkedListMahasiswa()
    list_mhs.tambah_data("Mahasiswa A")
    list_mhs.tambah_data("Mahasiswa B")
    list_mhs.tambah_data("Mahasiswa C")
    print("Urutan data:")
    list_mhs.tampilkan()
    print()

    print("=== 2. FITUR UNDO (Stack - LIFO) ===")
    undo_system = StackUndo()
    undo_system.lakukan_aksi("Input Nilai Budi")
    undo_system.lakukan_aksi("Hapus Data Ani")
    undo_system.undo()  
    print()

    print("=== 3. SISTEM ANTREAN (Queue - FIFO) ===")
    antrean = AntreanPengolahan()
    antrean.tambah_antrean("Cetak Transkrip NIM 101")
    antrean.tambah_antrean("Cetak Transkrip NIM 102")
    antrean.proses_antrean()  
    print()

    print("=== 4. PENCARIAN DATA BERDASARKAN KEY (Hash Table) ===")
    sistem_hash = SystemMahasiswaHash()
    sistem_hash.tambah_mahasiswa("123001", "Budi Santoso", "Teknik Informatika")
    sistem_hash.tambah_mahasiswa("123002", "Siti Aminah", "Sistem Informasi")
    
    sistem_hash.cari_by_nim("123001")