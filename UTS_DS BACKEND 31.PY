#List
adat= ["Puter Kayun","Ngopi Sepuluh Ewu","Seblang Bakungan"]
wisata = ["Baluran","Djawatan","Pulau Merah"]
desa = ["Kemiren","Alasmalang","Gombengsari"]
pesanan = []

#Menu Utama
print ("==========================================MENU UTAMA=================================================")
print (" ")
print ("  Kota Gandrung terletak di provinsi JAWA TIMUR, Kota tersebut bernama Kota Banyuwangi,")
print ("  Sekarang Kamu ingin mengunjungi ADAT ISTIADAT, OBJEK WISATA, DESA ADAT di Kabupaten Banyuwangi ?  ")
print("=====================================================================================================")

#Inputan 
print ("Tuliskan Nama Kamu :")
nama = input()
print (" ")
print ("Tuliskan Alamat Kamu")
alamat = input()
print (" ")
print ("12+15")
print ("Berapa Hasil dari Penjumlahan Tersebut ?")
print ("Jawaban Kamu :")
umur = input()
if umur == ("27"):
    print (" ")
    print ("Yeay! Jawaban Kamu Benar")
    print (" ")
    print ("Selamat Datang di PROGRAM PEMESANAN TIKET")
    print (" ")
else:
    print ("Sayang sekali, jawaban kamu salah!")
    print ("Kamu dilarang masuk")
    print ("Terima Kasih")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    exit()

#Perulangan
while True:
    menu = input("===   1. Adat Istiadat   ===\n===   2. Objek Wisata    ===\n===   3. Desa Adat       ===\n Masukkan menu [1-3]: ")
    if menu == "1":
        print("\nAnda memilih Menu 1 yaitu Adat Istiadat")
        print("Pilih Adat Istiadat anda :")
        while True:
            for ii in range(0, len(adat)):
                print(f'{ii + 1}. {adat[ii]}')
            list_adat = int(input('Pilih Menu 1-3: '))
            if list_adat == 1:
                pesanan.append(adat[0])
                print('\n==== List Tempat Tujuan ====')
                for a in range(0, len(pesanan)):
                    print(f'{a +1}. {pesanan[a]} x1 tiket kunjungan')
                break
            elif list_adat == 2:
                pesanan.append(adat[1])
                print('\n==== List Tempat Tujuan ====')
                for a in range(0, len(pesanan)):
                    print(f'{a +1}. {pesanan[a]} x1 tiket kunjungan')
                break
            elif list_adat == 3:
                pesanan.append(adat[2])
                print('\n==== List Tempat Tujuan ====')
                for a in range(0, len(pesanan)):
                    print(f'{a +1} {pesanan[a]} x1 tiket kunjungan')
                break
            else:
                print("Silahkan masukkan menu yang tersedia")
                continue
    elif menu == "2":
        print("\nAnda memilih Menu 2 yaitu wisata")
        print("Pilih wisata anda :")
        while True:
            for ii in range(0, len(wisata)):
                print(f'{ii + 1}. {wisata[ii]}')
            list_wisata = int(input('Pilih Menu 1-3: '))
            if list_wisata == 1:
                pesanan.append(wisata[0])
                print('\n==== List Tempat Tujuan ====')
                for a in range(0, len(pesanan)):
                    print(f'{a +1}. {pesanan[a]} x1 tiket kunjungan')
                break
            elif list_wisata == 2:
                pesanan.append(wisata[1])
                print('\n==== List Tempat Tujuan ====')
                for a in range(0, len(pesanan)):
                    print(f'{a +1}. {pesanan[a]} x1 tiket kunjungan')
                break
            elif list_wisata == 3:
                pesanan.append(wisata[2])
                print('\n==== List Tempat Tujuan ====')
                for a in range(0, len(pesanan)):
                    print(f'{a +1}. {pesanan[a]} x1 tiket kunjungan')
                break
            else:
                print("Silahkan masukkan menu yang tersedia")
                continue
    elif menu == "3":
        print("\nAnda memilih Menu 3 yaitu desa")
        print("Pilih desa anda :")
        while True:
            for ii in range(0, len(desa)):
                print(f'{ii + 1}. {desa[ii]}')
            list_desa = int(input('Pilih Menu 1-3: '))
            if list_desa == 1:
                pesanan.append(desa[0])
                print('\n==== List Tempat Tujuan ====')
                for a in range(0, len(pesanan)):
                    print(f'{a +1}. {pesanan[a]} x1 tiket kunjungan')
                break
            elif list_desa == 2:
                pesanan.append(desa[1])
                print('\n==== List Tempat Tujuan ====')
                for a in range(0, len(pesanan)):
                    print(f'{a +1}. {pesanan[a]} x1 tiket kunjungan')
                break
            elif list_desa == 3:
                pesanan.append(desa[2])
                print('\n==== List Tempat Tujuan ====')
                for a in range(0, len(pesanan)):
                    print(f'{a +1}. {pesanan[a]} x1 tiket kunjungan')
                break
            else:
                print("Silahkan masukkan menu yang tersedia")
                continue
    else:
        print("Menu Tidak ada\n")
        continue
    
    tambah = input('Ada yang ingin ditambahkan[Y/N]? ')
    if tambah == "Y" or tambah == "y":
        continue
    else:
        print("\nTerimakasih atas kunjungan anda. Selamat Menikmati Liburan Anda")
        break 
