from prettytable import PrettyTable
import pyinputplus as pyip

karyawan = {}
def login():
    usr = "admin"
    pwd = "12345"

    cek = 3

    while cek > 0:
        garis()
        print("LOGIN SISTEM DATA KARYAWAN")
        garis()

        username = pyip.inputStr("Masukkan Username: ", blank=False)
        password = pyip.inputPassword("Masukkan Password: ", mask="*")

        if username != usr:
            cek -= 1
            print(f"Username salah. Sisa percobaan: {cek}")
        elif password != pwd:
            cek -= 1
            print(f"Password salah. Sisa percobaan: {cek}")
        else:
            print("Login Berhasil!")
            return True

    print("Anda gagal login 3 kali")
    return False

def garis():
    print("=" * 50)

def tampil(pilih = "0", nama = None):
    garis()
    print("MENU TAMPIL DATA KARYAWAN")
    garis()
    
    if not karyawan:
        print("Belum ada data karyawan")
        return
    
    table = PrettyTable()
    if pilih == "0":
        
        table.field_names = ["ID", "Nama", "Tempat, Tanggal Lahir",  "Jabatan",  "Bagian"]
        for idk, dd in karyawan.items():
            table.add_rows(
                    [
                        [idk,
                         dd["nama"].title(),
                         dd["ttl"].title(),
                         dd["jabatan"],
                         dd["bagian"]]
                    ]
                )
        print(table)
    elif pilih != "0": 
        if pilih in karyawan:    
            table.field_names = ["ID", "Nama", "Tempat, Tanggal Lahir",  "Jabatan",  "Bagian"]
            table.add_row([
                pilih,
                karyawan[pilih]["nama"].title(),
                karyawan[pilih]["ttl"].title(),
                karyawan[pilih]["jabatan"],
                karyawan[pilih]["bagian"]
                               ])
            print(table)
        
        else:
            print("ID tidak ditemukan")
        
def search_karyawan(nama=None, jabatan=None, bagian=None):
    garis()
    print("MENU SEARCH DATA KARYAWAN")
    garis()
    if not karyawan:
        print("Belum ada data karyawan")
        return
    
    table = PrettyTable()
    table.field_names = ["ID", "Nama", "Tempat, Tanggal Lahir", "Jabatan", "Bagian"]

    ditemukan = False

    for idk, dd in karyawan.items():

        cocok = True
        if nama is not None:
            if nama.lower() not in dd["nama"].lower():
                cocok = False

        if jabatan is not None:
            if dd["jabatan"] != jabatan:
                cocok = False

        if bagian is not None:
            if dd["bagian"] != bagian:
                cocok = False

        if cocok:
            table.add_row([
                idk,
                dd["nama"].title(),
                dd["ttl"].title(),
                dd["jabatan"],
                dd["bagian"]
            ])
            ditemukan = True

    if ditemukan:
        print(table)
    else:
        print("Data tidak ditemukan")

def jumlah_karyawan_bagian():
    garis()
    print("MENU JUMLAH KARYAWAN PER BAGIAN")
    garis()

    if not karyawan:
        print("Belum ada data karyawan")
        return

    data_bagian = {}

    for idk, dd in karyawan.items():
        bagian = dd["bagian"]

        if bagian in data_bagian:
            data_bagian[bagian] += 1
        else:
            data_bagian[bagian] = 1

    for bagian, jumlah in data_bagian.items():
        print(f"{bagian} : {jumlah} orang")

def menu_data():
    garis()
    print("Menu Tampil Karyawan")
    garis()
    while True:
        opsi_search = pyip.inputMenu(["Tampil Seluruh Data", "Search Data Karyawan" , "Jumlah Karyawan Perbagian", "Keluar Menu Tampil Data"], prompt="Pilih Menu berikut: \n", numbered=True)
        if opsi_search == "Tampil Seluruh Data":
            tampil()
            break
        elif opsi_search == "Search Data Karyawan":
            while True:
                opsi_search = pyip.inputMenu(["Nama", "Jabatan", "Bagian", "Keluar Menu Tampil Data"], prompt="Anda Search Data Karyawan berdasarkan Apa?: \n", numbered=True)
                if opsi_search == "Nama":
                    nama = input("Masukkan Nama yang ingin anda cari :")
                    search_karyawan(nama)
                    continue
                elif opsi_search == "Jabatan":
                    jabatan = menu_jabatan()
                    search_karyawan(jabatan = jabatan)
                    continue
                elif opsi_search == "Bagian":
                    bagian = menu_bagian()
                    search_karyawan(bagian = bagian)
                    continue
                elif opsi_search == "Keluar Menu Tampil Data":
                    break
        elif opsi_search == "Jumlah Karyawan Perbagian":
            jumlah_karyawan_bagian()
            continue
        elif opsi_search == "Keluar Menu Tampil Data":
            print("Anda Kembali ke Menu Awal")
            break

        
def validasi_tgl():
    while True:    
        while True:
            tgl = input("Masukkan Tanggal Lahir dengan Format(ddmmyyyy): ")
            if len(tgl) != 8:
                print("Panjang input tanggal lahir salah")
                continue
            if not tgl.isnumeric():
                print("Tanggal Lahir bukan angka")
                continue
            else:
                tgl_lahir = tgl
                break

        tanggal = int(tgl_lahir[0:2])
        tgl_str = tgl_lahir[0:2]
        bulan = tgl_lahir[2:4]
        tahun = int(tgl_lahir[4:])

        if tahun > 2007 or tahun < 1990:
            print("umur tidak memenuhi kriteria")
            continue
        elif int(bulan) < 1 or int(bulan) > 12:
            print("bulan tersebut tidak ada")
            continue
        elif tanggal < 1:
            print("tanggal tersebut tidak ada")
            continue
        elif (bulan == "02") and ((tahun % 4 != 0 and tanggal > 28) or (tahun % 4 == 0 and tanggal > 29)):
            print("tanggal tersebut tidak ada")
            continue
        elif (bulan in ["04", "06", "09", "11"]) and (tanggal > 30): 
            print ("tanggal tersebut tidak ada")
            continue   
        elif tanggal > 31:
            print ("tanggal tersebut tidak ada")
            continue
        else:
            tgl_lahir_akhir = f"{tgl_str}-{bulan}-{tahun}"
            return tgl_lahir_akhir

def menu_jabatan():
    jabatan = pyip.inputMenu(["Magang", "Staff", "Lower Manager", "Top Manager"], prompt="Masukkan Jabatan: \n", numbered=True)
    return jabatan

def menu_bagian():
    bagian = pyip.inputMenu(["Bagian Produksi", "Bagian Penjualan", "Bagian Tata Usaha"], prompt="Masukkan Bagian: \n", numbered=True)
    return bagian

def tambah():
    garis()
    print("Menu Tambah Data Karyawan")
    garis()
    f = True
    while f:
        nama = input("Masukkan Nama Karyawan: ").lower()
        tpt_lahir = input("Masukkan Kota Lahir: ").lower()
        tgl_lahir = validasi_tgl()
        jabatan = menu_jabatan()
        bagian = menu_bagian()

        print(f"""
Nama : {nama.title()}
Tempat, tanggal lahir : {tpt_lahir.title()}, {tgl_lahir}
Jabatan : {jabatan}
Bagian : {bagian}
""")
        while True:
            konf = input("Apakah data sudah benar? y/n: ").lower()
            if konf == "y" or konf == "ya":
                if not karyawan:
                    nomor_baru = 1
                else:
                    semua_nomor = []
                    for idk in karyawan.keys():
                        angka = int(idk[1:])   # ambil angka setelah huruf A
                        semua_nomor.append(angka)

                    nomor_baru = max(semua_nomor) + 1
                id = f"A{'0'*(3 - len(str(nomor_baru)))}{nomor_baru}"
                karyawan[id] = {"nama" : nama, "ttl" : f"{tpt_lahir}, {tgl_lahir}", "jabatan" : jabatan, "bagian" : bagian}
                print("Tambah Karyawan Berhasil")
                f = False
                break
            elif konf == "n" or konf == "no":
                print("Masukkan data yang benar")
                break
            else:
                print("tidak terdapat opsi tersebut")

def update_data():
    garis()
    print("MENU RUBAH DATA KARYAWAN")
    garis()
    table1 = PrettyTable()
    def opsi_rubah(opsi, id = "1", ubahdict = "1", ubahbr = "1"):
        if opsi != "Tempat, Tanggal Lahir":
            print(f"{karyawan[id]}, {karyawan[id]['nama'].title()}")
            table1.field_names = [f"{ubahdict.title()} Lama", f"{ubahdict.title()} Baru"]
            table1.add_row([karyawan[id][ubahdict], ubahbr])
            print(table1)
            table1.clear_rows()
            konf = pyip.inputMenu(["Ya", "Tidak"], prompt=f"Apakah anda yakin ingin merubah {opsi}? \n", numbered=True,)
            if konf.lower() == "ya":
                karyawan[id][ubahdict] = ubahbr
                print(f"Update {ubahdict.title()} Berhasil")
                print("Anda Kembali Ke Menu Awal")
                return False
            if konf.lower() == "tidak":
                return True
        else:    
            f2 = True
            while f2:
                tpt_lahir = input("Masukkan Tempat Lahir Karyawan: ").lower()
                tgl_lahir = validasi_tgl()
                table1.field_names = ["Tempat, Tanggal Lahir Lama", "Tempat, Tanggal Lahir Baru"]
                table1.add_row([karyawan[id]["ttl"].title(), f"{tpt_lahir.title()}, {tgl_lahir}"])
                print(table1)
                konf2 = pyip.inputMenu(["Ya", "Tidak"], prompt="Apakah anda yakin ingin merubah Tempat, Tanggal Lahir?", numbered=True)
                if konf2.lower() == "ya":
                    karyawan[id]["ttl"] = f"{tpt_lahir.title()}, {tgl_lahir}"
                    print("Update Tempat, Tanggal Lahir Berhasil")
                    print("Anda Kembali Ke Menu Awal")
                    f2 = False
                    return False
                if konf2.lower() == "tidak":
                    return True
    tampil()
    f = True
    while f:
        id = input("Masukkan Id karyawan yang akan dirubah data(ketik 'keluar' jika ingin ke halaman awal): ").upper()
        if id.lower() == "keluar":
            print("Anda Kembali Ke Menu Awal")
            break

        elif id not in karyawan:
            print("id karyawan tersebut tidak terdaftar")
            continue

        else:
            tampil(id)
            opsi_ubah = pyip.inputMenu(["Promosi/Demosi", "Rubah Data Diri Karyawan", "Pindah Bagian", "Kembali Pilih Karyawan", "Kembali Menu Awal"], prompt="Masukkan pilihan rubah data anda: \n", numbered=True)
            if opsi_ubah == "Promosi/Demosi":
                while True:
                    jabatan = menu_jabatan()
                    a = "jabatan"
                    if jabatan == karyawan[id][a]:
                        print("Jabatan Tidak Berubah")
                        continue
                    else:
                        if opsi_rubah("jabatan",id,a,jabatan) == False:
                            f = False
                            break
                        else:
                            continue

            elif opsi_ubah == "Rubah Data Diri Karyawan":
                opsi_dd = pyip.inputMenu(["Nama", "Tempat, Tanggal Lahir"], prompt="Apa yang ingin anda rubah: \n", numbered=True)
                if opsi_dd == "Nama":
                    while True:
                        nama = input("Masukkan Nama Karyawan: ").lower()    
                        a = "nama"
                        if nama == karyawan[id][a]:
                            print("Nama tidak berubah")
                            continue
                        else:
                            if opsi_rubah(opsi_dd, id, a, nama) == False:
                                f = False
                                break
                            else:
                                continue

                elif opsi_dd == "Tempat, Tanggal Lahir":
                    if opsi_rubah(opsi_dd, id) == False:
                        f = False
                        break
            
            elif opsi_ubah == "Pindah Bagian":
                while True:
                    bagian = menu_bagian()
                    a = "bagian"
                    if bagian == karyawan[id][a]:
                        print("Bagian Tidak Berubah")
                        continue
                    else:
                        if opsi_rubah("bagian",id,a,bagian) == False:
                            f = False
                            break
                        else:
                            continue
            elif opsi_ubah == "Kembali Pilih Karyawan":
                continue
            elif opsi_ubah == "Kembali Menu Awal":
                print("Anda Kembali Ke Menu Awal")
                break

def hapus():
    garis()
    print("MENU HAPUS DATA KARYAWAN")
    garis()
    tampil()
    while True:
        id = input("Masukkan ID Karyawan yang datanya akan dihapus: ")
        if id.lower() == "keluar":
            print("Anda Kembali Ke Menu Awal")
            break
        elif id.upper() not in karyawan:
            print("Data Tidak ada")
            continue
        else:
            tampil(id.upper())
            konf = pyip.inputMenu(["Ya", "Tidak"], prompt="Apakah anda yakin ingin Menghapus Data Karyawan tersebut?\n", numbered=True)
            if konf == "Ya":
                karyawan.pop(id.upper())
                print("Data Berhasil Dihapus")
                print("Anda kembali ke menu awal")
                break
            else:
                continue
def data_karyawan():
    if login():
        while True:
            garis()
            print("APLIKASI OLAH DATA KARYAWAN")
            garis()
            menu = pyip.inputMenu(["Tampil Data Karyawan", "Tambah Data Karyawan", "Rubah Data Karyawan", "Hapus Data Karyawan", "Keluar Program"], prompt="Silahkan pilih Menu: \n", numbered=True)
            if menu == "Tampil Data Karyawan":
                menu_data()
                continue
            elif menu == "Tambah Data Karyawan":
                tambah()
                continue
            elif menu == "Rubah Data Karyawan":
                update_data()
                continue
            elif menu == "Hapus Data Karyawan":
                hapus()
                continue
            elif menu == "Keluar Program":
                print("Anda Keluar Program, Terima Kasih")
                break
    else: 
        print("Anda Keluar Program, Terima Kasih")

    

data_karyawan()
