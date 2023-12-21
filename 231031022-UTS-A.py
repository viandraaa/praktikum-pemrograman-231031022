'''UTS
1. Buat variabel jenis list berikut.
    
    BIO =  ['Nama Lengkap',
            'NIM',
            'Tanggal-Bulan-Tahun Lahir'
            'aktif'
            'S1',
            'Sistem Informasi A',
            '2023-2024',
            'ganjil'
            'Institut Teknologi Bacharuddin Jusuf Habibie',
            'Parepare',
            'Jurusan Sains',
            'kartu rencana studi mahasiswa']
            #(NOTED: sesuaikan dengan data anda)
            
2. Buat variabel jenis nested list berikut.

MK =   [['22A1209','22A1210','22A1211','22A1212','22A1213','22A1214','22A1215','22A1216',],
        ['Matkul1','Matkul2','Matkul3','Matkul4','Matkul5','Matkul6','Matkul7','Matkul8'],
        [2,3,3,2,3,3,3,2],
        ['Selasa','Senin','Rabu','Senin','Kamis','Kamis','Kamis','Kamis'],
        ['07.30-09.10','07.30-09.10','07.30-09.10','07.30-09.10','07.30-09.10','07.30-09.10','07.30-09.10','07.30-09.10']]

#(NOTED: Ubah Nama Matakuliah, Jumlah SKS, waktu kuliah, dan jadwal)
        
3. Susun Kode dengan hasil runing seperti berikut.
           
            
             INSTITUT TEKNOLOGI BACHARUDDIN JUSUF HABIBIE
                        JURUSAN SAINS PROGRAM
                    KARTU RENCANA STUDI MAHASISWA
                           GANJIL 2023/2024

                    
Nama Lengkap    : NAMA LENGKAP
NIM             : 60022010
Program/prodi   : S1/Sistem Informasi A
Tahun Masuk     : 2023 Ganjil
Status          : Aktif
|--|--  10  --|--           26         --|--5--|-- 8  --|--    13   --|
-----------------------------------------------------------------------
No. Kode      |      Mata Kuliah         | SKS |  Hari  |    Jadwal   |
-----------------------------------------------------------------------
1   22A1209   | Matkul1                  |  2  | Senin  |  07.30-09.10|
2   22A1210   | Matkul2                  |  3  | Selasa |  07.30-09.10|
3   22A1211   | Matkul3                  |  3  | Rabu   |  07.30-09.10|
4   22A1212   | Matkul4                  |  2  | Senin  |  07.30-09.10|
5   22A1213   | Matkul5                  |  3  | Kamis  |  07.30-09.10|
6   22A1214   | Matkul6                  |  3  | Kamis  |  07.30-09.10|
7   22A1215   | Matkul7                  |  3  | Kamis  |  07.30-09.10|
8   22A1216   | Matkul8                  |  2  | Kamis  |  07.30-09.10|
-----------------------------------------------------------------------
                        TOTAL SKS           21                        |
-----------------------------------------------------------------------
|---------------------------------71-----------------------------------|
Summary:
Jumlah Mata Kuliah       : 8
Jumlah Mata Kuliah 2 SKS : 3 Mata Kuliah
Jumlah Mata Kuliah 3 SKS : 5 Mata kuliah
Mata Kuliah hari Senin   : 2 Mata Kuliah
Mata Kuliah hari Selasa  : 1 Mata Kuliah
Mata Kuliah hari Rabu    : 1 Mata Kuliah
Mata Kuliah hari Kamis   : 1 Mata Kuliah
Mata Kuliah hari Jumat   : 0 Mata Kuliah
                                              Parepare, 25 Oktober 2023



                                                     NAMA LENGKAP      
                                                     ------------
'''


# Tulis Kode Jawaban di bawah!


bio =  ['Viandra Maryam Azzahra',
            '231031022',
            '02-02-2005',
            'aktif',
            'S1',
            'Sistem Informasi A',
            '2023-2024',
            'ganjil',
            'Institut Teknologi Bacharuddin Jusuf Habibie',
            'Parepare',
            'Jurusan Sains',
            'kartu rencana studi mahasiswa']

MK =   [['22A1209','22A1210','22A1211','22A1212','22A1213','22A1214','22A1215','22A1216',],
        ['Pengantar Pemrograman','Kalkulus Dasar','Sainster','Bahasa','PTI','Cinta','Pancasila','Agama'],
        [3,2,2,3,3,2,2,3],
        ['Selasa','Selasa','Rabu','Kamis','Kamis','Kamis','Jumat','Jumat'],
        ['07.30-09.10','13.30-15.00','13.30-15.00','07.30-09.10','13.30-15.00','15.20-17.00','09.20-11.00','13.30-15.00']]

print(bio[-4].upper().center(71))
print(bio[-2].upper().center(71))
print(bio[-1].upper().center(71))
strr = bio[-5]+' '+bio[-6].replace('-','/')
print(strr.upper().center(71))



print(f'''
Nama Lengkap    : {bio[0].upper()}
NIM             : {bio[1]}
Program/prodi   : {bio[4]}/{bio[5]}
Tahun Masuk     : {bio[-5].title()} {bio[6]}
Status          : {bio[3]}''')

print('-'*69)
print('No.'+'|'+'Kode'.ljust(10)+'|'+'Mata Kuliah'.center(26)+'|'+'SKS'.center(5)+'|'+'Hari'.center(8)+'|'+'Jadwal'.center(13)+'|')
print('-'*69)
print('1. '+'|'+'22A1209'.ljust(10)+'|'+'Pengantar Pemrograman'.center(26)+'|'+'3'.center(5)+'|'+'Selasa'.center(8)+'|'+'07.30-09.10'.center(13)+'|')
print('2. '+'|'+'22A1210'.ljust(10)+'|'+'Kalkulus Dasar'.center(26)+'|'+'2'.center(5)+'|'+'Selasa'.center(8)+'|'+'13.30-15.00'.center(13)+'|')
print('3. '+'|'+'22A1211'.ljust(10)+'|'+'Sainster'.center(26)+'|'+'2'.center(5)+'|'+'Rabu'.center(8)+'|'+'13.30-15.00'.center(13)+'|')
print('4. '+'|'+'22A1212'.ljust(10)+'|'+'Bahasa'.center(26)+'|'+'3'.center(5)+'|'+'Kamis'.center(8)+'|'+'07.30-09.10'.center(13)+'|')
print('5. '+'|'+'22A1213'.ljust(10)+'|'+'PTI'.center(26)+'|'+'3'.center(5)+'|'+'Kamis'.center(8)+'|'+'13.30-15.00'.center(13)+'|')
print('6. '+'|'+'22A1214'.ljust(10)+'|'+'Cinta'.center(26)+'|'+'2'.center(5)+'|'+'Kamis'.center(8)+'|'+'15.20-17.00'.center(13)+'|')
print('7. '+'|'+'22A1215'.ljust(10)+'|'+'Pancasila'.center(26)+'|'+'2'.center(5)+'|'+'Jumat'.center(8)+'|'+'09.20-11.00'.center(13)+'|')
print('8. '+'|'+'22A1216'.ljust(10)+'|'+'Agama'.center(26)+'|'+'2'.center(5)+'|'+'Jumat'.center(8)+'|'+'13.30-15.00'.center(13)+'|')
print('-'*69)

totalsks=sum(MK[2])
print(f'\t\t        TOTAL SKS      21')
str1='69'
a=str1.center(69,'-')
print(a)
jumlah_matkul=len(MK[1])
matkul_2sks=MK[2].count(2)
matkul_3sks=MK[2].count(3)
matkul_selasa=MK[3].count('Selasa')
matkul_rabu=MK[3].count('Rabu')
matkul_kamis=MK[3].count('Kamis')
matkul_jumat=MK[3].count('Jumat')

print(f'''Summary:
Jumlah Mata Kuliah       : {len(MK[1])}
Jumlah Mata Kuliah 2 SKS : {matkul_2sks} Mata Kuliah
Jumlah Mata Kuliah 3 SKS : {matkul_3sks} Mata Kuliah
Mata Kuliah hari Selasa  : {matkul_selasa} Mata Kuliah
Mata Kuliah hari Rabu    : {matkul_rabu} Mata Kuliah
Mata Kuliah hari Kamis   : {matkul_kamis} Mata Kuliah
Mata Kuliah hari Jumat   : {matkul_jumat} Mata Kuliah''')

nama_kota = bio[9]
tanggal = bio[2]
mix = (nama_kota+", "+tanggal).rjust(72)
print(mix)
print("\n"*4)
nama = bio[0]
strip_akhir = "-"*12
print(nama.rjust(72))
print(strip_akhir.rjust(74))
