def hitung_subtotal(harga, jumlah, adalah_member=False):

    subtotal = harga * jumlah

    if adalah_member:
        subtotal = subtotal * 0.90

    return int(subtotal)


print("Selamat datang di Kasir Minimarket!")


# validasi status member
while True:
    status_member = input("Apakah Anda member? (y/n): ").strip().lower()

    if status_member == "y":
        adalah_member = True
        break
    elif status_member == "n":
        adalah_member = False
        break
    else:
        print("Input tidak valid. Masukkan y atau n.")


total = 0


while True:
    nama_barang = input("Masukkan nama barang (kosongkan untuk selesai): ").strip()

    # jika nama barang kosong, transaksi selesai
    if nama_barang == "":
        break

    # validasi harga
    while True:
        try:
            harga = int(input("Harga barang: "))

            if harga < 0:
                print("Harga tidak boleh negatif.")
                continue

            break

        except ValueError:
            print("Harga harus berupa angka.")


    # validasi jumlah
    while True:
        try:
            jumlah = int(input("Jumlah barang: "))

            if jumlah <= 0:
                print("Jumlah barang harus lebih dari 0.")
                continue

            break

        except ValueError:
            print("Jumlah barang harus berupa angka.")


    subtotal = hitung_subtotal(harga, jumlah, adalah_member)

    total += subtotal

    print(f"Subtotal {nama_barang}: Rp{subtotal}")


print(f"Total belanja: Rp{total}")
                