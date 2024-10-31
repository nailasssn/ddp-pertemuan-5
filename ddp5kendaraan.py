# Buat variabel list dengan value : [namaKendaraan, JenisKendaraan, ccKendaraan, warna kendaraan, roda kendaraan]
kendaraan = ['beat pop', 'sepeda ontel', 21, 'merah', 2]
print('kendaraan saya')
print(kendaraan[3])
print('=========')

# tambahkan dari list tsb di nelakang dengan value : [harga kendaraan, tipe kendaraan]
kendaraan.append(25000000)
kendaraan.append ('metic')
print(kendaraan)
print('=========')

# tambahkan setelah jenis kendaraan dengan value [merk kendaraan]
kendaraan.insert(2, 'beat')
print(kendaraan)
print("=========")


# Buat program python dengan match case untuk menghitung luas bangun datar : 
#jika pilih 1, maka menghitung luas persegi 
#jika pilih 2, maka menghitung luas lingkaran 
#jika pilih 3, maka menghitung luas segitiga 
#Kalau pilihannya tidak ada maka ada keterangan : salah pilih

print('ini adalah program sederhana untuk menghitung luas bangun datar')
print('pilih menu angka 1-3 : \n1. Persegi\n2. Lingkaran\n3. Segitiga')
pilihmenu = int(input('silahkann pilih menu dengan mengetikan angka 1-3'))

match pilihmenu:
    # case 1
      # proses
    case 1:
      print('menghitung luas persegi')
      sisi = int(input('Silahkan masukan sisi persegi'))
      hitung = sisi * sisi
      print(f'Luas persegi adalah : {hitung}')
      
    #case 2
      # proses
    case 2:
      print('menghitung luas lingkaran')
      r = int(input('masukan nilai jari jari lingkaran'))
      hitung = 22/7 * r**2
      print(f'Luas lingkaran adalah : {hitung}')
      
    # case 3  
      # proses
    case 3:
      print('menghitung luas segitiga')
      alas = int(input('Masukan nilai alas'))
      tinggi = int(input('Masukan nilai tinggi'))
      hitung = 1/2 * alas * tinggi
      print(f'Luas Segitiga adalah : {hitung}')
    # case akhir
      # proses
    case _:
      print('Pilihan tidak valid, silahkan pilih antara 1-3')
