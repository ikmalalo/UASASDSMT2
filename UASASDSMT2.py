from prettytable import PrettyTable
from colorama import Fore, Back, Style
import datetime

user = {}
emoney = {}
produk = {
    "makanan": {"Big Mac🍔": 50000, "McNuggets🥐": 30000, "Tripler Burger With Cheese🍔": 60000, "McChicken🍗": 32000, "McSpicy🍗": 33000},
    "minuman": {"Coca Cola🥤": 10000, "Fanta🍷": 10000, "Sprite🍸": 10000, "Fruit Tea🧃": 12000},
    "escream": {"Sundae🍧": 15000, "McFlurry🍨": 20000, "Cone🍦": 7000},
    "happy_meal": {"Hamburger Happy Meal🍔": 35000, "4 Piece Chicken McNuggets Happy Meal🥐": 30000, "6 Piece Chicken McNuggets Happy Meal🥠": 35000}
}

def menu_registrasi():
    print(Back.BLUE + Fore.WHITE + Style.BRIGHT + "+--------------------------------------------------+" + Style.RESET_ALL)
    print(Back.BLUE + Fore.WHITE + Style.BRIGHT + "|  Silahkan Registrasi Sebelum Melakukan Login 🙂  |" + Style.RESET_ALL)
    print(Back.BLUE + Fore.WHITE + Style.BRIGHT + "+--------------------------------------------------+" + Style.RESET_ALL)
    while True:
        nama = str(input("Masukkan Nama: "))
        if nama:
            break
        else:
            print(Fore.RED + Style.BRIGHT + "Nama tidak boleh kosong. Silahkan masukkan nama.😡")
            print(Style.RESET_ALL)
    while True:
        password = str(input("Masukkan Password: "))
        if password:
            break
        else:
            print(Fore.RED + Style.BRIGHT + "Password tidak boleh kosong. Silahkan masukkan password.😡")
            print(Style.RESET_ALL)
    while True:
        try:
            umur = int(input("Masukkan Umur: "))
            break
        except ValueError:
            print(Fore.RED + Style.BRIGHT + "Inputan harus berupa angka. Silahkan masukkan umur yang valid.😡")
            print(Style.RESET_ALL)
    while True:
        print("Pilih Gender Pria/Wanita")
        print("1. Pria")
        print("2. Wanita")
        gender_input = input("Pilih Gender anda (1/2): ")
        if gender_input.isdigit() and gender_input in ['1', '2']:
            gender = "Pria" if gender_input == '1' else "Wanita"
            break
        else:
            print(Fore.RED + Style.BRIGHT + "Harus Input memakai Angka😡")
            print(Style.RESET_ALL)
    user[nama] = {"password": password, "umur": umur, "gender": gender, "pesanan": [], "riwayat": []}
    emoney[nama] = 0 
    if umur < 10:
        sapaan = "adek👼"
    elif gender == "Pria":
        sapaan = "mas👨"
    else:
        sapaan = "mbak👩"
    print(Fore.GREEN + Style.BRIGHT + f"Registrasi sukses, Silahkan Lanjut login {sapaan} {nama}!🤗\n" + Style.RESET_ALL)

def menu_login():
    print(Back.LIGHTCYAN_EX + Fore.WHITE + Style.BRIGHT + "+--------------------------------------------------+" + Style.RESET_ALL)
    print(Back.LIGHTCYAN_EX + Fore.WHITE + Style.BRIGHT + "|  Silahkan Login Jika SUdah Registrasi🙂          |" + Style.RESET_ALL)
    print(Back.LIGHTCYAN_EX + Fore.WHITE + Style.BRIGHT + "+--------------------------------------------------+" + Style.RESET_ALL)
    nama = str(input("Masukkan Nama: "))
    password = str(input("Masukkan Password: "))
    if nama == "admin" and password == "admin123":
        menu_admin()
    elif nama in user and user[nama]["password"] == password:
        current_user = user[nama]
        if current_user["umur"] < 10:
            sapaan = "adek👼"
        elif current_user["gender"] == "Pria":
            sapaan = "mas👨"
        else:
            sapaan = "mbak👩"
        print(Style.BRIGHT + f"Selamat datang🤗 {sapaan} {nama} ! Usia anda saat ini adalah {current_user['umur']} tahun!\n" + Style.RESET_ALL)
        menu_user(nama)
    else:
        print(Fore.RED + Style.BRIGHT + "Login gagal, nama atau password salah.🤨🫵\n")
        print(Style.RESET_ALL)

def menu_user(nama):
    while True:
        print(Fore.CYAN + Style.BRIGHT)
        print("+---------------------------------------------------+")
        print("|     Silahkan Pilih Menu Opsi yang tersedia😉👌    |")
        print("+---------------------------------------------------+")
        print("|                 1. Pesan Makanan🍔                |")
        print("|                 2. Pesan EsCream 🍨               |")
        print("|                 3. Pesan Minum🥤                  |")
        print("|                 4. Lihat Checkout🛍️                |")
        print("|                 5. Bayar💵                        |")
        print("|                 6. Topup eMoney💳                 |")
        print("|                 7. Cek Saldo💲                    |")
        print("|                 8. Keluar🚪                       |")
        print("+---------------------------------------------------+")
        print("|           Jangan Lupa Memberi ⭐⭐⭐⭐⭐          |")
        print("|           Pada Aplikasi Kami💕                    |")
        print("+---------------------------------------------------+")
        try:
            pilihan = int(input("Pilih menu: "))
            if pilihan == 1:
                pesan_makanan(nama)
            elif pilihan == 2:
                pesan(nama, "escream")
            elif pilihan == 3:
                pesan(nama, "minuman")
            elif pilihan == 4:
                lihat_checkout(nama)
            elif pilihan == 5:
                bayar(nama)
            elif pilihan == 6:
                topup_emoney(nama)
            elif pilihan == 7:
                cek_saldo(nama)
            elif pilihan == 8:
                break
            else:
                print(Back.RED + Fore.BLACK + Style.BRIGHT + "Pilihan tidak valid, coba lagi.\n")
                print(Style.RESET_ALL)
        except ValueError:
            print(Back.RED + Fore.BLACK + Style.BRIGHT + "Harus Input Angka🔢." + Style.RESET_ALL)

def menu_admin():
    while True:
        print(Fore.MAGENTA + Style.BRIGHT)
        print("+--------------------------------------+")
        print("|     Selamat Datang adminku🤗!!!      |")
        print("|--------------------------------------|")
        print("|              Menu Admin              |")
        print("|--------------------------------------|")
        print("|           1. Tambah Menu             |")
        print("|           2. Hapus Menu              |")
        print("|           3. Edit Menu               |")
        print("|           4. Lihat Menu              |")
        print("|           5. Lihat Pembelian User    |")
        print("|           6. Keluar                  |")
        print("+--------------------------------------+" + Style.RESET_ALL)
        try:
            pilihan = int(input(Fore.MAGENTA + "Pilih menu: "))
            if pilihan == 1:
                tambah_menu()
            elif pilihan == 2:
                hapus_menu()
            elif pilihan == 3:
                edit_menu()
            elif pilihan == 4:
                lihat_menu()
            elif pilihan == 5:
                lihat_pembelian_user()
            elif pilihan == 6:
                break
            else:
                print(Back.RED + Style.BRIGHT + "Pilihan tidak valid, coba lagi.\n")
                print(Style.RESET_ALL)
        except ValueError:
            print(Back.RED + Fore.BLACK + Style.BRIGHT + "Harus Input Angka🔢." + Style.RESET_ALL)

            
def tambah_menu():
    print(Fore.MAGENTA + Style.BRIGHT + "\nTambah Menu:" + Style.RESET_ALL)
    print(Fore.MAGENTA + "1. Makanan")
    print("2. Minuman")
    print("3. EsCream")
    pilihan = int(input("Pilih kategori: "))
    if pilihan == 1:
        kategori = "makanan"
    elif pilihan == 2:
        kategori = "minuman"
    elif pilihan == 3:
        kategori = "escream"
    else:
        print(Fore.RED + Style.BRIGHT + "Pilihan tidak valid❌. Coba Lagi\n")
        print(Style.RESET_ALL)
        return
    nama = str(input("Masukkan nama produk: "))
    while True:
        try:
            harga = int(input(Fore.MAGENTA + "Masukkan harga produk: Rp" + Style.RESET_ALL))
            break
        except ValueError:
            print(Back.RED + Fore.BLACK + Style.BRIGHT + "Harus Input Angka🔢." + Style.RESET_ALL)
    produk[kategori][nama] = harga
    print(f"{nama} berhasil ditambahkan ke menu {kategori}.\n")
    tampilkan_produk(kategori)


def hapus_menu():
    print(Fore.MAGENTA + Style.BRIGHT + "Hapus Menu:" + Style.RESET_ALL)
    print(Fore.MAGENTA + "1. Makanan")
    print("2. Minuman")
    print("3. EsCream")
    
    try:
        pilihan = int(input("Pilih kategori: "))
        if pilihan == 1:
            kategori = "makanan"
        elif pilihan == 2:
            kategori = "minuman"
        elif pilihan == 3:
            kategori = "escream"
        else:
            print(Fore.RED + Style.BRIGHT + "Pilihan tidak valid❌. Coba Lagi\n" + Style.RESET_ALL)
            return
        
        if kategori in produk and len(produk[kategori]) > 0:
            tampilkan_produk(kategori)
            
            try:
                index = int(input(Fore.MAGENTA + "Masukkan nomor produk yang ingin dihapus: ")) - 1
                if 0 <= index < len(produk[kategori]):
                    nama_produk = list(produk[kategori].keys())[index]
                    del produk[kategori][nama_produk]
                    print(Fore.GREEN + Style.BRIGHT + f"{nama_produk} berhasil dihapus dari menu {kategori}.\n" + Style.RESET_ALL)
                    tampilkan_produk(kategori)
                else:
                    print(Fore.RED + Style.BRIGHT + "Nomor produk tidak ada.\n" + Style.RESET_ALL)
            except ValueError:
                print(Back.RED + Fore.BLACK + Style.BRIGHT + "Harus Input Angka🔢.\n" + Style.RESET_ALL)
        else:
            print(Fore.RED + Style.BRIGHT + "Kategori produk kosong atau tidak ada.\n" + Style.RESET_ALL)
    
    except ValueError:
        print(Back.RED + Fore.BLACK + Style.BRIGHT + "Harus Input Angka🔢.\n" + Style.RESET_ALL)


def edit_menu():
    print(Style.BRIGHT + "Edit Menu:" + Style.RESET_ALL)
    print(Fore.MAGENTA + "1. Makanan")
    print("2. Minuman")
    print("3. EsCream")   
    try:
        pilihan = int(input("Pilih kategori: "))
        if pilihan == 1:
            kategori = "makanan"
        elif pilihan == 2:
            kategori = "minuman"
        elif pilihan == 3:
            kategori = "escream"
        else:
            print(Fore.RED + Style.BRIGHT + "Pilihan tidak valid❌. Coba Lagi\n" + Style.RESET_ALL)
            return       
        if kategori in produk and len(produk[kategori]) > 0:
            tampilkan_produk(kategori)
            try:
                index = int(input(Fore.MAGENTA + "Masukkan nomor produk yang ingin diedit: ")) - 1
                if 0 <= index < len(produk[kategori]):
                    nama_produk = list(produk[kategori].keys())[index]
                    
                    while True:
                        try:
                            harga_baru = int(input(Fore.MAGENTA + "Masukkan harga baru produk: Rp"))
                            break
                        except ValueError:
                            print(Fore.RED + Style.BRIGHT + "Inputan harus berupa angka🔢. Silahkan masukkan harga yang valid." + Style.RESET_ALL)                  
                    produk[kategori][nama_produk] = harga_baru
                    print(Fore.GREEN + Style.BRIGHT + f"Harga {nama_produk} berhasil diperbarui menjadi Rp{harga_baru}.\n" + Style.RESET_ALL)
                    tampilkan_produk(kategori)
                else:
                    print(Fore.RED + Style.BRIGHT + "Nomor produk tidak ada.\n" + Style.RESET_ALL)
            except ValueError:
                print(Back.RED + Fore.BLACK + Style.BRIGHT + "Harus Input Angka🔢.\n" + Style.RESET_ALL)
        else:
            print(Fore.RED + Style.BRIGHT + "Kategori produk kosong atau tidak ada.\n" + Style.RESET_ALL)
    except ValueError:
        print(Back.RED + Fore.BLACK + Style.BRIGHT + "Harus Input Angka🔢.\n" + Style.RESET_ALL)

def lihat_menu():
    print("Lihat Menu:")
    print("1. Makanan")
    print("2. Minuman")
    print("3. EsCream")
    try:
        pilihan = int(input("Pilih kategori: "))
        if pilihan == 1:
            kategori = "makanan"
        elif pilihan == 2:
            kategori = "minuman"
        elif pilihan == 3:
            kategori = "escream"
        else:
            print(Fore.RED + Style.BRIGHT + "Pilihan tidak valid❌. Coba Lagi.\n" + Style.RESET_ALL)
            return
        tampilkan_produk(kategori)
    except ValueError:
        print(Back.RED + Fore.BLACK + Style.BRIGHT + "Harus Input Angka🔢." + Style.RESET_ALL)
        print(Style.RESET_ALL)


def lihat_pembelian_user():
    print(Fore.MAGENTA + Style.BRIGHT + "Lihat Pembelian User")
    table = PrettyTable([ "Nama User", "nama produk", "Harga"])
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
        print(Fore.RED + Style.BRIGHT + "Belum ada pembelian hari ini❌.\n")

def tampilkan_produk(kategori):
    print(Fore.YELLOW + Style.BRIGHT)
    table = PrettyTable(["No", "Nama Produk", "Harga"])
    for i, (nama_produk, harga) in enumerate(produk[kategori].items(), start=1):
        table.add_row([i, nama_produk, harga])
    print(table)
    print(Style.RESET_ALL)
    
def pesan_makanan(nama):
    user_umur = user[nama]["umur"]
    if user_umur < 10:
        print("1. Happy Meal👼🍴")
        print("2. Menu Biasa👨👩")
        pilihan = int(input("Pilih menu (ketik 0 untuk kembali ke menu utama): "))
        if pilihan == 1:
            print("Menu Happy Meal:")
            tampilkan_produk("happy_meal")
            pesanan_idx = int(input(Fore.CYAN + Style.BRIGHT +"Masukkan nomor produk yang ingin dipesan (atau ketik '0' untuk kembali ke menu): " + Style.RESET_ALL))
            if pesanan_idx == 0:
                return
            try:
                pesanan_idx = int(pesanan_idx) - 1
                semua_produk = list(produk["happy_meal"].items())
                pesanan = semua_produk[pesanan_idx][0]
                harga = semua_produk[pesanan_idx][1]
                user[nama]["pesanan"].append((pesanan, harga))
                print(Fore.GREEN + Style.BRIGHT + f"{pesanan} telah ditambahkan ke pesanan Anda.\n")
            except (ValueError, IndexError):
                print(Fore.RED + Style.BRIGHT + "Produk tidak ditemukan, coba lagi.\n")
                print(Style.RESET_ALL)
        elif pilihan == "2":
            print("Menu Makanan:")
            tampilkan_produk("makanan")
            pesanan_idx = input(Fore.CYAN + Style.BRIGHT + "Masukkan nomor produk yang ingin dipesan (atau ketik '0' untuk kembali ke menu): "+ Style.RESET_ALL)
            if pesanan_idx == 0:
                return
            try:
                pesanan_idx = int(pesanan_idx) - 1
                semua_produk = list(produk["makanan"].items())
                pesanan = semua_produk[pesanan_idx][0]
                harga = semua_produk[pesanan_idx][1]
                user[nama]["pesanan"].append((pesanan, harga))
                print(Fore.GREEN + Style.BRIGHT + f"{pesanan} telah ditambahkan ke pesanan Anda.\n")
            except (ValueError, IndexError):
                print(Fore.RED + Style.BRIGHT + "Produk tidak ditemukan, coba lagi.\n")
                print(Style.RESET_ALL)
        else:
            print(Back.RED + Style.BRIGHT + "Pilihan tidak valid, coba lagi.\n")
            print(Style.RESET_ALL)
    else:
        pesan(nama, "makanan")

def pesan(nama, kategori):
    print(f"Menu {kategori.capitalize()}:")
    tampilkan_produk(kategori)
    while True:
        pesanan_idx_input = input(Fore.CYAN + Style.BRIGHT + "Masukkan nomor produk yang ingin dipesan (atau ketik '0' untuk kembali ke menu): " + Style.RESET_ALL)
        if pesanan_idx_input == '0':
            return
        try:
            pesanan_idx = int(pesanan_idx_input) - 1
            if pesanan_idx >= 0:
                semua_produk = list(produk[kategori].items())
                pesanan = semua_produk[pesanan_idx][0]
                harga = semua_produk[pesanan_idx][1]
                user[nama]["pesanan"].append((pesanan, harga))
                print(Fore.GREEN + Style.BRIGHT + f"{pesanan} telah ditambahkan ke pesanan Anda.\n")
                break
            else:
                print(Fore.RED + Style.BRIGHT + "Nomor produk tidak valid. Silakan masukkan nomor produk yang benar atau ketik '0' untuk kembali ke menu.\n" + Style.RESET_ALL)
        except (ValueError, IndexError):
            print(Fore.RED + Style.BRIGHT + "Produk tidak ditemukan, coba lagi.\n" + Style.RESET_ALL)

def lihat_checkout(nama):
    if not user[nama]["pesanan"]:
        print(Fore.RED + Style.BRIGHT + "Anda belum memesan apapun.\n")
        print(Style.RESET_ALL)
        return
    total_harga = sum([nama_produk[1] for nama_produk in user[nama]["pesanan"]])
    print(Fore.YELLOW + Style.BRIGHT +"----- Checkout -----")
    table = PrettyTable([Fore.YELLOW + Style.BRIGHT + "Nama Produk", "Harga"])
    for nama_produk, harga in user[nama]["pesanan"]:
        table.add_row([nama_produk, harga])
    print(table)
    print(Fore.YELLOW + Style.BRIGHT + f"Total harga sementara: Rp{total_harga}" + Style.RESET_ALL)
    print(Fore.YELLOW + Style.BRIGHT +"-------------------\n" + Style.RESET_ALL)

def bayar(nama):
    if not user[nama]["pesanan"]:
        print(Fore.RED + Style.BRIGHT + "Anda belum memesan apapun.\n" + Style.RESET_ALL)
        return
    total_harga = sum([nama_produk[1] for nama_produk in user[nama]["pesanan"]])
    if total_harga > 350000:
        total_harga *= 0.75
        print(Fore.GREEN + Style.BRIGHT + "Anda mendapatkan diskon 25% karena total pembelian lebih dari Rp350.000\n" + Style.RESET_ALL)
    if user[nama]["umur"] < 10:
        print(Fore.GREEN + Style.BRIGHT + "Anda mendapatkan Happy Meal dan bonus mainan karena berusia di bawah 10 tahun.\n" + Style.RESET_ALL)
    print(f"Total harga: Rp{total_harga}")
    print(f"Saldo eMoney: Rp{emoney[nama]}")
    if emoney[nama] < total_harga:
        print(Fore.RED + Style.BRIGHT + "Saldo eMoney tidak cukup.\n" + Style.RESET_ALL)
        while True:
            print(Fore.CYAN + Style.BRIGHT +"1. Topup eMoney💳")
            print("2. Batalkan Pembelian")
            try:
                pilihan = int(input("Pilih opsi: "))
                if pilihan == 1:
                    topup_emoney(nama)
                    break
                elif pilihan == 2:
                    user[nama]["pesanan"] = []
                    print("Pembelian dibatalkan.\n")
                    return
                else:
                    print(Fore.RED + Style.BRIGHT + "Pilihan tidak valid. Silakan pilih opsi 1 atau 2.\n" + Style.RESET_ALL)
            except ValueError:
                print(Fore.RED + Style.BRIGHT + "Harus input angka.❌ Silakan pilih opsi 1 atau 2.\n" + Style.RESET_ALL)
    emoney[nama] -= total_harga
    user[nama]["riwayat"].extend(user[nama]["pesanan"])
    print(Fore.GREEN + Style.BRIGHT + "Pembayaran berhasil.\n" + Style.RESET_ALL)
    cetak_invoice(nama, total_harga)

def topup_emoney(nama):
    while True:
        try:
            jumlah = int(input(Fore.CYAN + Style.BRIGHT + "Masukkan jumlah topup: Rp."))
            break
        except ValueError:
            print(Fore.RED + Style.BRIGHT + "Inputan harus berupa angka. Silahkan masukkan jumlah topup yang valid.")
            print(Style.RESET_ALL)
    emoney[nama] += jumlah
    print(Fore.GREEN + Style.BRIGHT + f"Topup berhasil. Saldo eMoney Anda sekarang: Rp{emoney[nama]}\n" + Style.RESET_ALL)

def cek_saldo(nama):
    print(Fore.CYAN + Style.BRIGHT + f"Saldo eMoney Anda: Rp.{emoney[nama]}\n" + Style.RESET_ALL)

def cetak_invoice(nama, total_harga):
    print(Fore.YELLOW + Style.BRIGHT)
    current_user = user[nama]
    pesanan = current_user.get("pesanan", [])
    table = PrettyTable(["Nama Produk", "Harga"])
    for nama_produk, harga in pesanan:
        table.add_row([nama_produk, harga])
    print(table)
    print(Style.BRIGHT + "=============================================")
    print(f"Total harga : Rp{total_harga}")
    print(f"Saldo sisa  : Rp.{emoney[nama]}")
    user[nama]["pesanan"] = []
    print(Style.BRIGHT + "=============================================")
    print(f"Nama        : {nama}")
    print(f"Gender      : {current_user['gender']}                         ")
    print(f"Usia        : {current_user['umur']} tahun")
    print(f"Waktu       : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=============================================")
    print(Style.RESET_ALL)

def main():
    while True:
        now = datetime.datetime.now()
        if now.hour < 9 or now.hour >= 23:
            print(Fore.LIGHTRED_EX + Style.BRIGHT + "+------------------------------------------------------------------------+")
            print("|          Mohon Maaf Kami Hanya Buka Pada Jam 09:00🕘 Dan 23:00🕚       |")
            print("|                            Harap Menunggu 😙                           |")
            print("+------------------------------------------------------------------------+" + Style.RESET_ALL)
            break
        
        print(Fore.YELLOW + Style.BRIGHT + "+-----------------------------------------+")
        print("|Selamat datang di McDonald's Online🍔🍟🍗|")
        print("|-----------------------------------------|")
        print("|              1. Registrasi📝            |")
        print("|              2. Login🍴                 |")
        print("|              3. Keluar🚪                |")
        print("|-----------------------------------------|")
        print("|          Contact Us = 📞 14045          |")
        print("+-----------------------------------------+" + Style.RESET_ALL)
        try:
            pilihan = int(input(Fore.YELLOW + "Pilih menu: "))
            print(Style.RESET_ALL)
            if pilihan == 1:
                menu_registrasi()
            elif pilihan == 2:
                menu_login()
            elif pilihan == 3:
                print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "+------------------------------------------------------------------------+")
                print("|   Terimakasih Sudah Mengunjungi Aplikasi Kami Jangan Lupa ⭐⭐⭐⭐⭐   |")
                print("|                       Sampai Jumpa Kembali😙🥰😘                       |")
                print("+------------------------------------------------------------------------+")
                break
            else:
                print(Back.RED + Fore.BLACK + Style.BRIGHT + "Pilihan tidak valid, coba lagi.")
                print(Style.RESET_ALL)
        except ValueError:
            print(Back.RED + Fore.BLACK + Style.BRIGHT + "Harus Input Angka🔢." + Style.RESET_ALL)
            print(Style.RESET_ALL)


if __name__ == "__main__":
    main()
