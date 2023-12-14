print()

# A.PENJUMLAHAN WAKTU

from datetime import datetime, timedelta

# Masukkan waktu pertama
time_str1 = input("Masukkan waktu pertama (hh:mm): ")
hours1, minutes1, = map(int, time_str1.split(':'))

# Masukkan waktu kedua
time_str2 = input("Masukkan waktu kedua (hh:mm): ")
hours2, minutes2, = map(int, time_str2.split(':'))

# Buat objek timedelta untuk masing-masing waktu
time1 = timedelta(hours=hours1, minutes=minutes1,)
time2 = timedelta(hours=hours2, minutes=minutes2,)

# Jumlahkan waktu
total_time = time1 + time2

# Konversi hasil ke format jam:menit:
total_hours, remainder = divmod(total_time.seconds, 3600)
total_minutes, total_seconds = divmod(remainder, 60)

print(f"Waktu Sekarang menunjukkan Pukul: {total_hours:02d}:{total_minutes:02d}")
    
# B.PROGRAM SELISIH WAKTU

from datetime import datetime, timedelta

# Masukkan waktu pertama
time_str1 = input("Masukkan waktu pertama (hh:mm): ")
hours1, minutes1, = map(int, time_str1.split(':'))

# Masukkan waktu yang dikurangkan
time_str2 = input("Jumlah waktu yang dikurangkan (hh:mm): ")
hours2, minutes2, = map(int, time_str2.split(':'))

# Objek timedelta untuk masing-masing waktu
time1 = timedelta(hours=hours1, minutes=minutes1,)
time2 = timedelta(hours=hours2, minutes=minutes2,)

# Selisih waktu
total_time = time1 - time2

# Konversi hasil ke format jam:menit:
total_hours, remainder = divmod(total_time.seconds, 3600)
total_minutes, total_seconds = divmod(remainder, 60)

print(f"Waktu Sekarang menunjukkan Pukul: {total_hours:02d}:{total_minutes:02d}")
