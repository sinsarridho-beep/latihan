daftar_buku = []


def tambah_buku():
    jdl = input("Masukkan Judul: ")
    pnl = input("Masukkan Penulis: ")
    buku_baru = {"judul": jdl, "penulis": pnl}
    
    daftar_buku.append(buku_baru)
    print("Buku berhasil ditambahkan!")

def lihat_buku():
    print("\n--- DAFTAR BUKU ---")
    if not daftar_buku:
        print("Belum ada buku.")
        return

    for nomor, buku in enumerate(daftar_buku, start=1):
        print(f"{nomor}. {buku['judul']} - {buku['penulis']}")


while True:
    print("\n--- MENU PERPUSTAKAAN ---")
    print("1. Tambah Buku")
    print("2. Lihat Buku")
    print("3. Keluar")
    pilihan = input("Pilih menu (1/2/3): ")

    if pilihan == "1":
        tambah_buku()
    elif pilihan == "2":
        lihat_buku()
    elif pilihan == "3":
        print("Keluar dari aplikasi...")
        break
    else:
        print("Pilihan tidak valid!")