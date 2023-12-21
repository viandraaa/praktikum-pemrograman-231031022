#variabel a diinstalisasi dengan nilai True]
a = True

#perulangan while dengan kondisi a
while a:
#definisikan variabel a dengan nilai true
    pilih = input('Pilihan:')
#program memeriksa nilai yang dimasukkan oleh pengguna
    if pilih == 'ya':
        print('Selamat Datang')
        break
    elif pilih == 'tidak':
        print ('Sampai Jumpa')
        break
    else:
        print('Pilihan tidak valid')
        
