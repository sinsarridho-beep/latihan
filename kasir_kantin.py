print("=== Kasir Kantin V1 ===")
total_belanja = int(input("Total Belanja: Rp "))
member = input("Apakah punya kartu member? (ya/tidak): ")

diskon = 0

# MULAI LOGIKA NESTED IF DI SINI:
if member == "ya":
    # Cek belanja pakai if lagi di sini (ingat indentasi)
    if total_belanja >= 100000:
        diskon = total_belanja * 0.1
    else:
        diskon = 0
else:
    if total_belanja >= 200000:
        diskon = total_belanja * 0.2
    else:
        diskon = 0

total_bayar = total_belanja - diskon
print("Total yang harus dibayar: Rp " + str(total_bayar))