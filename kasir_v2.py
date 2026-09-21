print("=== Kasir Kantin V2 ===")
total_belanja = 0

while True:
    input_harga = input("Masukkan harga barang (ketik 'selesai' untuk total): ")

    if input_harga == "selesai":
        break

    total_belanja = total_belanja + int(input_harga)

print("Total Belanja Anda: Rp " + str(total_belanja))