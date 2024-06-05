from prettytable import PrettyTable

user = {}
emoney = {}
produk = {
    "makanan": {"Big Mac": 50000, "McNuggets": 30000, "Tripler Burger With Cheese": 60000, "McChicken": 32000, "McNugget": 24000, "McSpidy": 33000},
    "minuman": {"Coca Cola": 10000, "Fanta": 10000, "Sprite": 10000, "Fruit Tea": 12000},
    "escream": {"Sundae": 15000, "McFlurry": 20000, "Cone": 7000},
    "happy_meal": {"Hamburger Happy Meal": 35000, "4 Piece Chicken McNuggets Happy Meal": 30000, "6 Piece Chicken McNuggets Happy Meal": 35000}
}

def menu_registrasi():
    print("Silahkan Registrasi Sebelum Melakukan Login")

    while True:
        nama = input("Masukkan Nama: ")
        if nama:
            break
        else:
            print("Nama tidak boleh kosong. Silahkan masukkan nama.")
    while True:
        password = input("Masukkan Password: ")
        if password:
            break
        else:
            print("Password tidak boleh kosong. Silahkan masukkan password.")
    while True:
        try:
            umur = int(input("Masukkan Umur: "))
            break
        except ValueError:
            print("Inputan harus berupa angka. Silahkan masukkan umur yang valid.")

    print("Pilih Gender Pria/Wanita")
    print("1. Pria")
    print("2. Wanita")

    while True:
        gender = input("Pilih Gender anda (1/2): ")
        if gender == "1" or gender == "2":
            gender = "Pria" if gender == "1" else "Wanita"
            break
        else:
            print("Pilihan tidak valid. Silahkan pilih 1 untuk Pria atau 2 untuk Wanita.")
    
    user[nama] = {"password": password, "umur": umur, "gender": gender, "pesanan": [], "riwayat": []}
    emoney[nama] = 0 
    print(f"Registrasi sukses, Silahkan Lanjut login{nama}!\n")

def menu_login():
    print("Silahkan Login Jika Sudah Registrasi")
    nama = input("Masukkan Nama: ")
    password = input("Masukkan Password: ")
    if nama == "admin" and password == "admin123":
        menu_admin()
    elif nama in user and user[nama]["password"] == password:
        current_user = user[nama]
        if current_user["umur"] < 10:
            sapaan = "adek"
        elif current_user["gender"] == "Pria":
            sapaan = "mas"
        else:
            sapaan = "mbak"
        print(f"Selamat datang, {sapaan} {nama}! Usia anda saat ini adalah {current_user['umur']} tahun!\n")
        menu_user(nama)
    else:
        print("Login gagal, nama atau password salah.\n")

def menu_user(nama):
    while True:
        print("Silahkan Pilih Menu Opsi yang tersedia :")
        print("1. Pesan Makanan")
        print("2. Pesan EsCream")
        print("3. Pesan Minum")
        print("4. Lihat Checkout")
        print("5. Bayar")
        print("6. Topup eMoney")
        print("7. Cek Saldo")
        print("8. Keluar")
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            pesan_makanan(nama)
        elif pilihan == "2":
            pesan(nama, "escream")
        elif pilihan == "3":
            pesan(nama, "minuman")
        elif pilihan == "4":
            lihat_checkout(nama)
        elif pilihan == "5":
            bayar(nama)
        elif pilihan == "6":
            topup_emoney(nama)
        elif pilihan == "7":
            cek_saldo(nama)
        elif pilihan == "8":
            break
        else:
            print("Pilihan tidak valid, coba lagi.\n")

def menu_admin():
    while True:
        print("Selamat Datang adminku!!!")
        print("Menu Admin:")
        print("1. Tambah Menu")
        print("2. Hapus Menu")
        print("3. Edit Menu")
        print("4. Lihat Menu")
        print("5. Lihat Pembelian User")
        print("6. Keluar")
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            tambah_menu()
        elif pilihan == "2":
            hapus_menu()
        elif pilihan == "3":
            edit_menu()
        elif pilihan == "4":
            lihat_menu()
        elif pilihan == "5":
            lihat_pembelian_user()
        elif pilihan == "6":
            break
        else:
            print("Pilihan tidak valid, coba lagi.\n")

def tambah_menu():
    print("Tambah Menu:")
    print("1. Makanan")
    print("2. Minuman")
    print("3. EsCream")
    pilihan = input("Pilih kategori: ")
    if pilihan == "1":
        kategori = "makanan"
    elif pilihan == "2":
        kategori = "minuman"
    elif pilihan == "3":
        kategori = "escream"
    else:
        print("Pilihan tidak valid.\n")
        return
    nama = input("Masukkan nama produk: ")
    while True:
        try:
            harga = int(input("Masukkan harga produk: Rp"))
            break
        except ValueError:
            print("Inputan harus berupa angka. Silahkan masukkan harga yang valid.")
    
    produk[kategori][nama] = harga
    print(f"{nama} berhasil ditambahkan ke menu {kategori}.\n")

def hapus_menu():
    print("Hapus Menu:")
    print("1. Makanan")
    print("2. Minuman")
    print("3. EsCream")
    pilihan = input("Pilih kategori: ")
    if pilihan == "1":
        kategori = "makanan"
    elif pilihan == "2":
        kategori = "minuman"
    elif pilihan == "3":
        kategori = "escream"
    else:
        print("Pilihan tidak valid.\n")
        return
    tampilkan_produk(kategori)
    nama = input("Masukkan nama produk yang ingin dihapus: ")
    if nama in produk[kategori]:
        del produk[kategori][nama]
        print(f"{nama} berhasil dihapus dari menu {kategori}.\n")
    else:
        print(f"{nama} tidak ditemukan di menu {kategori}.\n")

def edit_menu():
    print("Edit Menu:")
    print("1. Makanan")
    print("2. Minuman")
    print("3. EsCream")
    pilihan = input("Pilih kategori: ")
    if pilihan == "1":
        kategori = "makanan"
    elif pilihan == "2":
        kategori = "minuman"
    elif pilihan == "3":
        kategori = "escream"
    else:
        print("Pilihan tidak valid. COba Lagi\n")
        return
    tampilkan_produk(kategori)
    nama = input("Masukkan nama produk yang ingin diedit: ")
    if nama in produk[kategori]:
        while True:
            try:
                harga_baru = int(input("Masukkan harga baru produk: Rp"))
                break
            except ValueError:
                print("Inputan harus berupa angka. Silahkan masukkan harga yang valid.")
        produk[kategori][nama] = harga_baru
        print(f"Harga {nama} berhasil diperbarui menjadi Rp{harga_baru}.\n")
    else:
        print(f"{nama} tidak ditemukan di menu {kategori}.\n")

def lihat_menu():
    print("Lihat Menu:")
    print("1. Makanan")
    print("2. Minuman")
    print("3. EsCream")
    pilihan = input("Pilih kategori: ")
    if pilihan == "1":
        kategori = "makanan"
    elif pilihan == "2":
        kategori = "minuman"
    elif pilihan == "3":
        kategori = "escream"
    else:
        print("Pilihan tidak valid.\n")
        return
    tampilkan_produk(kategori)

def lihat_pembelian_user():
    print("Lihat Pembelian User")
    table = PrettyTable(["Nama User", "nama produk", "Harga"])
    ada_pembelian = False
    for nama, data in user.items():
        if "riwayat" in data and data["riwayat"]:
            ada_pembelian = True
            for nama_produk, harga in data["riwayat"]:
                table.add_row([nama, nama_produk, harga])
    
    if ada_pembelian:
        print(table)
        print("Pembelian user ditampilkan di atas.\n")
    else:
        print("Belum ada pembelian hari ini.\n")

def tampilkan_produk(kategori):
    table = PrettyTable(["No", "Nama Produk", "Harga"])
    for i, (nama_produk, harga) in enumerate(produk[kategori].items(), start=1):
        table.add_row([i, nama_produk, harga])
    print(table)

def pesan_makanan(nama):
    user_umur = user[nama]["umur"]
    if user_umur < 10:
        print("1. Happy Meal")
        print("2. Menu Biasa")
        pilihan = input("Pilih menu (ketik '0' untuk kembali ke menu utama): ")
        if pilihan == "1":
            print("Menu Happy Meal:")
            tampilkan_produk("happy_meal")
            pesanan_idx = input("Masukkan nomor produk yang ingin dipesan (atau ketik '0' untuk kembali ke menu): ")
            if pesanan_idx == "0":
                return
            try:
                pesanan_idx = int(pesanan_idx) - 1
                semua_produk = list(produk["happy_meal"].items())
                pesanan = semua_produk[pesanan_idx][0]
                harga = semua_produk[pesanan_idx][1]
                user[nama]["pesanan"].append((pesanan, harga))
                print(f"{pesanan} telah ditambahkan ke pesanan Anda.\n")
            except (ValueError, IndexError):
                print("Produk tidak ditemukan, coba lagi.\n")
        elif pilihan == "2":
            print("Menu Makanan:")
            tampilkan_produk("makanan")
            pesanan_idx = input("Masukkan nomor produk yang ingin dipesan (atau ketik '0' untuk kembali ke menu): ")
            if pesanan_idx == "0":
                return
            try:
                pesanan_idx = int(pesanan_idx) - 1
                semua_produk = list(produk["makanan"].items())
                pesanan = semua_produk[pesanan_idx][0]
                harga = semua_produk[pesanan_idx][1]
                user[nama]["pesanan"].append((pesanan, harga))
                print(f"{pesanan} telah ditambahkan ke pesanan Anda.\n")
            except (ValueError, IndexError):
                print("Produk tidak ditemukan, coba lagi.\n")
        else:
            print("Pilihan tidak valid, coba lagi.\n")
    else:
        pesan(nama, "makanan")

def pesan(nama, kategori):
    print(f"Menu {kategori.capitalize()}:")
    tampilkan_produk(kategori)
    pesanan_idx = input("Masukkan nomor produk yang ingin dipesan (atau ketik '0' untuk kembali ke menu): ")
    if pesanan_idx == "0":
        return
    try:
        pesanan_idx = int(pesanan_idx) - 1
        semua_produk = list(produk[kategori].items())
        pesanan = semua_produk[pesanan_idx][0]
        harga = semua_produk[pesanan_idx][1]
        user[nama]["pesanan"].append((pesanan, harga))
        print(f"{pesanan} telah ditambahkan ke pesanan Anda.\n")
    except (ValueError, IndexError):
        print("Produk tidak ditemukan, coba lagi.\n")

def lihat_checkout(nama):
    if not user[nama]["pesanan"]:
        print("Anda belum memesan apapun.\n")
        return
    total_harga = sum([nama_produk[1] for nama_produk in user[nama]["pesanan"]])
    print("----- Checkout -----")
    table = PrettyTable(["Nama Produk", "Harga"])
    for nama_produk, harga in user[nama]["pesanan"]:
        table.add_row([nama_produk, harga])
    print(table)
    print(f"Total harga sementara: Rp{total_harga}")
    print("-------------------\n")

def bayar(nama):
    if not user[nama]["pesanan"]:
        print("Anda belum memesan apapun.\n")
        return
    total_harga = sum([nama_produk[1] for nama_produk in user[nama]["pesanan"]])
    if total_harga > 350000:
        total_harga *= 0.75
        print("Anda mendapatkan diskon 25% karena total pembelian lebih dari Rp350.000\n")
    if user[nama]["umur"] < 10:
        print("Anda mendapatkan Happy Meal dan bonus mainan karena berusia di bawah 10 tahun.\n")
    print(f"Total harga: Rp{total_harga}")
    print(f"Saldo eMoney: Rp{emoney[nama]}")
    if emoney[nama] < total_harga:
        print("Saldo eMoney tidak cukup.\n")
        print("1. Topup eMoney")
        print("2. Batalkan Pembelian")
        pilihan = input("Pilih opsi: ")
        if pilihan == "1":
            topup_emoney(nama)
        else:
            user[nama]["pesanan"] = []
            print("Pembelian dibatalkan.\n")
            return
    emoney[nama] -= total_harga
    user[nama]["riwayat"].extend(user[nama]["pesanan"])  # Pindahkan pesanan ke riwayat
    print("Pembayaran berhasil.\n")
    cetak_invoice(nama, total_harga)

def topup_emoney(nama):
    while True:
        try:
            jumlah = int(input("Masukkan jumlah topup: Rp"))
            break
        except ValueError:
            print("Inputan harus berupa angka. Silahkan masukkan jumlah topup yang valid.")
    emoney[nama] += jumlah
    print(f"Topup berhasil. Saldo eMoney Anda sekarang: Rp{emoney[nama]}\n")

def cek_saldo(nama):
    print(f"Saldo eMoney Anda: Rp{emoney[nama]}\n")

def cetak_invoice(nama, total_harga):
    current_user = user[nama]
    pesanan = current_user.get("pesanan", [])
    print("----- Invoice -----")
    print(f"Nama: {nama}")
    print(f"Gender: {current_user['gender']}")
    print(f"Usia: {current_user['umur']} tahun")
    print("Pesanan:")
    table = PrettyTable(["Nama Produk", "Harga"])
    for nama_produk, harga in pesanan:
        table.add_row([nama_produk, harga])
    print(table)
    print(f"Total harga: Rp{total_harga}")
    print("-------------------")
    user[nama]["pesanan"] = []

def main():
    while True:
        print("Selamat datang di McDonald's Online")
        print("1. Registrasi")
        print("2. Login")
        print("3. Keluar")
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            menu_registrasi()
        elif pilihan == "2":
            menu_login()
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid, coba lagi.\n")

if __name__ == "__main__":
    main()
