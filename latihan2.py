ilai = [80, 90, 'A', 70, 100, 'B']

total = 0
jumlah_data = 0

for n in nilai:
    try:
        # Coba ubah ke angka
        angka = float(n)
        total += angka
        jumlah_data += 1
    except ValueError:
        # Jika bukan angka, skip
        print(f"Data '{n}' dilewati (bukan angka).")
        continue

# Hitung rata-rata hanya dari data valid
if jumlah_data > 0:
    rata_rata = total / jumlah_data
    print("\nRata-rata dari data valid:", rata_rata)
else:
    print("Tidak ada data angka yang valid.")
