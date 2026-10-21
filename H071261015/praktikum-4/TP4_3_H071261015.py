def hitung_mundur(angka):
    
    """
    Function rekursif untuk menghitung mundur
    sampai angka 0.
    """

    print(angka)

    # base case
    if angka == 0:
        print("Luncurkan!")
        return

    # recursive case
    hitung_mundur(angka - 1)
help(hitung_mundur)
    

while True:
    try:
        angka_awal = int(input("Masukkan angka awal hitung mundur: "))

        if angka_awal < 0:
            print("Input tidak valid, angka tidak boleh negatif.")
            continue

        break

    except ValueError:
        print("Input harus berupa bilangan bulat.")

hitung_mundur(angka_awal)