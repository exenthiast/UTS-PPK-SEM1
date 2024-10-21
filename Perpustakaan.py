# NAMA : ALFIZ DESTA ARIANT PERMANA
# NIM  : 24/543220/SV/25173
# KELAS: A1

buku_perpustakaan = {}

while pilihan != 5:
  print("Sistem Perpustakaan")
  print("1. Tambah Buku")
  print("2. Pinjam Buku")
  print("3. Cek Stok Buku")
  print("4. Cari Buku")
  print("5. Keluar")

  pilihan = int(input("Masukkan Pilihan (1-5): "))

  if pilihan == 1:
    judul_buku = input("Masukkan Judul Buku:")
    stok_buku = int(input("Masukkan Stok Buku:"))
    if judul_buku in buku_perpustakaan:
      buku_perpustakaan[judul_buku] += stok_buku
    else:
      buku_perpustakaan[judul_buku] = stok_buku
    print(f"Buku '{judul_buku}' Telah Ditambahkan dengan Stok '{stok_buku}'")
  elif pilihan == 2:
    judul_buku = input("Masukkan Judul Buku yang ingin dipinjam:")
    if judul_buku in buku_perpustakaan:
      buku_perpustakaan[judul_buku] -= 1
      print(f"Buku '{judul_buku}' Berhasil Dipinjam")
    else:
      print(f"Buku '{judul_buku}' Tidak Tersedia atau stok habis")
  elif pilihan == 3:
    print("Stok Buku di Perpustakaan: ")
    if len(buku_perpustakaan) == 0:
      print("Tidak ada buku yang tersedia")
    else:
      for judul_buku, stok_buku in buku_perpustakaan.items():
        print(f"Judul: {judul_buku} - stok: {stok_buku}")
  elif pilihan == 4:
    judul_buku = input("Masukkan Judul Buku yang ingin dicari:")
    if judul_buku in buku_perpustakaan:
      print(f"Buku '{judul_buku}' Tersedia dengan Stok '{buku_perpustakaan[judul_buku]}'")
    else:
      print(f"Buku '{judul_buku}' Tidak ditemukan di Perpustakaan")
  elif pilihan == 5:
    print("Terima Kasih telah menggunakan sistem perpustakaan")
  else:
    print("Pilihan Tidak Valid, silahkan coba lagi")
    break

