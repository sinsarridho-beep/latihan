def tambah_buku(): pass
def lihat_buku(): pass

# Ini adalah Main Loop (Nyawa Aplikasi)
while True:
    print("\n--- MENU PERPUSTAKAAN ---")
    print("1. Tambah Buku\n2. Lihat Buku\n3. Keluar")
    pilihan = input("Pilih menu (1/2/3): ")

    if pilihan == "1":
       tambah_buku()
        
    elif pilihan == "2":
        lihat_buku()
    elif pilihan == "3":
        print("Keluar dari aplikasi...")
        break # Rem Darurat
    else:
        print("Pilihan tidak valid!")