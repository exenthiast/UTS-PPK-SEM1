# Nama		: Alfiz Desta Ariant Permana
# Kelas		: A1
# NIM		: 24/543220/SV/25173

nama_karyawan = ""
jenis_kelamin = ""
status_pekerjaan = ""
gaji = 0
bonus = 0
target_penjualan_tercapai = False
hak_cuti = 24
cuti_pernikahan = 3
cuti_melahirkan = 0
karyawan_list = []


while True:  
    print("---Menu Manajemen Karyawan---")
    print("1. Dashboard Karyawan")
    print("2. Tambah Karyawan")
    print("3. Edit Karyawan")
    print("4. Pecat Karyawan")
    print("5. Izin Cuti")
    print("6. Performa Karyawan")
    print("7. Keluar")
   
    pilihan = input("Pilih menu (1-7): ")

    if pilihan == "1":
        if len(karyawan_list) == 0:
            print("Belum ada karyawan.")
        else:
            for i, karyawan in enumerate(karyawan_list):
                print(f"{i+1}. Nama: {karyawan['nama']}, Status: {karyawan['status']}, Gaji: {karyawan['gaji']}")

    elif pilihan == "2":
        nama = input("Masukkan nama karyawan: ")
        jenis_kelamin = input("Jenis kelamin (L/P): ")
        status = input("Status pekerjaan (Manager/Pegawai/Sales): ")
       
        if status == "Manager":
            gaji = 20000000
        elif status == "Pegawai":
            gaji = 7000000
        elif status == "Sales":
            gaji = 10000000
        else:
            print("Status pekerjaan tidak valid.")
            continue
       
        karyawan = {
            "nama": nama,
            "jenis_kelamin": jenis_kelamin,
            "status": status,
            "gaji": gaji,
            "penjualan": 0,
            "sisa_cuti": 24
        }
       
        karyawan_list.append(karyawan)
        print(f"Karyawan {nama} berhasil ditambahkan.")

    elif pilihan == "3":
        nama = input("Masukkan nama karyawan yang ingin diedit: ")
        karyawan_ditemukan = False
        for karyawan in karyawan_list:
            if karyawan["nama"] == nama:
                karyawan_ditemukan = True
                nama_baru = input("Nama baru (tekan Enter jika tidak ingin mengubah): ")
                if nama_baru:
                    karyawan["nama"] = nama_baru
                jenis_kelamin_baru = input("Jenis kelamin baru (L/P, tekan Enter jika tidak ingin mengubah): ")
                if jenis_kelamin_baru:
                    karyawan["jenis_kelamin"] = jenis_kelamin_baru
                else:
                    print("Jenis kelamin tidak valid. Masukkan L atau P.")
                status_baru = input("Status baru (Manager/Pegawai/Sales, tekan Enter jika tidak ingin mengubah): ")
                if status_baru:
                    if status_baru == "Manager":
                        karyawan["status"] = status_baru
                        karyawan["gaji"] = 20000000
                    elif status_baru == "Pegawai":
                        karyawan["status"] = status_baru
                        karyawan["gaji"] = 7000000
                    elif status_baru == "Sales":
                        karyawan["status"] = status_baru
                        karyawan["gaji"] = 10000000
                    else:
                        print("Status tidak valid.")
                print(f"Data karyawan {nama} berhasil diubah.")
                break
        if not karyawan_ditemukan:
            print("Karyawan tidak ditemukan.")

    elif pilihan == "4":
        nama = input("Masukkan nama karyawan yang ingin dipecat: ")
        karyawan_ditemukan = False
        for i, karyawan in enumerate(karyawan_list):
            if karyawan["nama"] == nama:
                karyawan_ditemukan = True
                del karyawan_list[i]
                print(f"Karyawan {nama} berhasil dipecat.")
                break
        if not karyawan_ditemukan:
            print("Karyawan tidak ditemukan.")

    elif pilihan == "5":
        nama = input("Masukkan nama karyawan yang ingin cuti: ")
        karyawan_ditemukan = False
        for karyawan in karyawan_list:
            if karyawan["nama"] == nama:
                karyawan_ditemukan = True
                print("Jenis cuti: 1. Pernikahan (3 hari), 2. Melahirkan (90 hari perempuan/10 hari laki-laki), 3. Libur tahunan (24 hari)")
                jenis_cuti = input("Pilih jenis cuti (1-3): ")
               
                if jenis_cuti == "1":
                    cuti = 3
                elif jenis_cuti == "2":
                    if karyawan["jenis_kelamin"] == "P":
                        cuti = 90
                    elif karyawan["jenis_kelamin"] == "L":
                        cuti = 10
                elif jenis_cuti == "3":
                    cuti = 24
                else:
                    print("Jenis cuti tidak valid.")
                    continue
               
                if karyawan["sisa_cuti"] >= cuti:
                    karyawan["sisa_cuti"] -= cuti
                    print(f"Cuti berhasil diproses. Sisa cuti: {karyawan['sisa_cuti']} hari.")
                else:
                    print("Cuti tidak mencukupi.")
                break
        if not karyawan_ditemukan:
            print("Karyawan tidak ditemukan.")

    elif pilihan == "6":
        nama = input("Masukkan nama karyawan yang ingin dinilai: ")
        karyawan_ditemukan = False
        for karyawan in karyawan_list:
            if karyawan["nama"] == nama:
                karyawan_ditemukan = True
                if karyawan["status"] == "Manager" or karyawan["status"] == "Sales":
                    penjualan = int(input("Masukkan jumlah penjualan: "))
                    karyawan["penjualan"] = penjualan
                    if karyawan["status"] == "Manager" and penjualan >= 1000:
                        karyawan["gaji"] += 5000000
                        print(f"Bonus diberikan. Gaji baru: {karyawan['gaji']}")
                    elif karyawan["status"] == "Sales" and penjualan >= 100:
                        karyawan["gaji"] += 3000000
                        print(f"Bonus diberikan. Gaji baru: {karyawan['gaji']}")
                    else:
                        print("Tidak ada bonus.")
                else:
                    print("Pegawai tidak berhak bonus berdasarkan penjualan.")
                break
        if not karyawan_ditemukan:
            print("Karyawan tidak ditemukan.")

    elif pilihan == "7":
        print("Program selesai.")
        break
   
    else:
        print("Pilihan tidak valid. Coba lagi.")

