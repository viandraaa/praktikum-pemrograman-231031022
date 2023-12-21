#inisialisasi variabel
pw_benar = 'mhs_ith23'
a = True
limit = 3
i = 0

#perulangan vuntuk maksimal limit
while a:
    i+= 1
#meminta pengguna memasukkan password
    pw = input('masukkan password: ')
#memeriksa password
    if pw == pw_benar:
        print('selamat anda login')
    else:
        print('password salah!')
#memeriksa limit
        if i == limit:
            print('kesempatan anda habis')
            a= False
        else:
            print(f'kesempatan anda tersisa',limit-1)
