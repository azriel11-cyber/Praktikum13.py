try:
    # Input angka pertama
    a = float(input("Masukkan angka pertama: "))

    # Input angka kedua
    b = float(input("Masukkan angka kedua: "))

    # Input operator
    op = input("Masukkan operator (+, -, *, /): ")

    # Cek operator valid
    if op not in ['+', '-', '*', '/']:
        raise Exception("Operator tidak valid! Gunakan (+, -, *, /).")

    # Operasi perhitungan
    if op == '+':
        hasil = a + b
    elif op == '-':
        hasil = a - b
    elif op == '*':
        hasil = a * b
    elif op == '/':
        # Tangani pembagian dengan nol
        try:
            hasil = a / b
        except ZeroDivisionError:
            print("Error: Tidak bisa membagi dengan nol!")
            exit()

    print("Hasil:", hasil)

# Tangani input angka yang bukan angka
except ValueError:
    print("Error: Input harus berupa angka!")
    
# Tangani exception lainnya (misal operator tidak valid)
except Exception as e:
    print("Error:", e)
