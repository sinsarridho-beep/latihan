user = input("Username: ")
pw = input("Password: ")

# Ganti tanda tanya (?) dengan logika and
if user == "admin" and pw == "telkom123":
    print("Login Berhasil! Selamat datang Admin.")
else:
    print("Login Gagal. Username atau Password salah.")