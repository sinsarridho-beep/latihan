# Anggaplah kita sudah punya 1 buku di database
daftar_buku = [{"judul": "Bumi Manusia", "penulis": "Pramoedya"}]

def hapus_buku():
    indeks = int(input("Masukkan nomor buku yang mau dihapus: "))
    
    # Karena user melihat buku pertama sebagai nomor 1,
    # sedangkan Python mulai dari 0, kita kurangi 1.
    indeks_asli = indeks - 1
    
    daftar_buku.pop(indeks_asli)
    print("Buku berhasil dihapus!")

hapus_buku()