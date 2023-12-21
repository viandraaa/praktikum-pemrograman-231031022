pendapatan = int(input("Pendapatan: "))
persentase = 0
bonus = 0
if pendapatan <= 5000:
    persentase = 50
elif pendapatan <= 4000:
    persentase = 40
elif pendapatan <= 3000:
    persentase = 30
elif pendapatan <= 2000:
    persentase = 20
elif pendapatan <= 1000:
    persentase = 10
else:
    persentase = 0
bonus = (pendapatan * persentase) / 100
total = pendapatan + bonus

print(f'Pendapatan: {pendapatan}')
print(f'Persentase: {persentase}%')
print(f'Bonus: {bonus}')
print(f'Jumlah Total: {total}')
