print("=== Sistem Akademik Tel-U ===")
nama = input("Masukkan nama: ")
absensi = int(input("Persentase Absen (0-100): "))
nilai = float(input("Nilai Akhir (0-100): "))

# MULAI TULIS LOGIKA IF-ELIF-ELSE DI BAWAH INI:
if absensi < 75:
    print("Gagal...")
else:
    if nilai >= 80:
        print("Grade A")
    elif nilai >= 70:
        print("Grade B")
    else:
        print("Grade C...")