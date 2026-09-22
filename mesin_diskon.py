def hitung_diskon(harga, persen):
    potongan = harga * (persen / 100)
    return potongan

harga_baju = 100000
diskonnya = hitung_diskon(harga_baju, 50)

harga_akhir = harga_baju - diskonnya
print("Harga yang harus dibayar: Rp " + str(harga_akhir))