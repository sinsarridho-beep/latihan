print("Aplikasi sedang berjalan...")

while True:
    jawaban = input("Apakah kamu yakin ingin keluar? (y/n): ")
    
    if jawaban == "y":
        # Tulis perintah rem darurat di bawah ini:
        print("Rem darurat diaktifkan!")
        break
    else:
        print("Input salah atau dibatalkan. Program dilanjutkan!")

print("Program Berhenti. Sampai jumpa!")