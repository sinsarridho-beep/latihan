daftar_buku = []

def tambah_buku():
    jdl = input("Judul: ")
    daftar_buku.append({"judul": jdl})
    print("Buku ditambahkan!")

def lihat_buku():
    print("\n--- DAFTAR BUKU ---")
    if not daftar_buku:
        print("Belum ada buku.")
        return

    for nomor, buku in enumerate(daftar_buku, start=1):
        print(f"{nomor}. {buku['judul']}")

def hapus_buku():
    if not daftar_buku:
        print("Belum ada buku yang bisa dihapus.")
        return

    try:
        indeks = int(input("Nomor Hapus: ")) - 1
    except ValueError:
        print("Nomor harus berupa angka!")
        return

    if indeks >= 0 and indeks < len(daftar_buku):
        daftar_buku.pop(indeks)
        print("Dihapus!")
    else:
        print("Salah nomor!")

# --- MAIN MENU ---
while True:
    print("\n1. Tambah  2. Lihat  3. Hapus  4. Keluar")
    pilihan = input("Pilih: ")

    if pilihan == "1":
        tambah_buku()
    elif pilihan == "2":
        lihat_buku()
    elif pilihan == "3":
        hapus_buku()
    elif pilihan == "4":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid!")