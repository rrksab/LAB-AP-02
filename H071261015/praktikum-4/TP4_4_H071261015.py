def konversi_suhu(suhu, skala_asal, skala_tujuan):

    skala_valid = ("C", "F", "K")

    # validasi skala asal
    if skala_asal not in skala_valid:
        raise ValueError("Skala suhu tidak dikenali.")

    # validasi skala tujuan
    if skala_tujuan not in skala_valid:
        raise ValueError("Skala suhu tidak dikenali.")


    # ubah suhu asal menjadi celsius
    if skala_asal == "C":
        celsius = suhu

    elif skala_asal == "F":
        celsius = (suhu - 32) * 5 / 9

    else:  # kelvin
        celsius = suhu - 273.15


    # ubah celsius ke skala tujuan
    if skala_tujuan == "C":
        hasil = celsius

    elif skala_tujuan == "F":
        hasil = (celsius * 9 / 5) + 32

    else:  # kelvin
        hasil = celsius + 273.15


    return hasil


print("=== Konversi Suhu ===")


while True:
    input_suhu = input("Masukkan suhu (atau 'selesai' untuk keluar): ").strip()

    # program selesai
    if input_suhu.lower() == "selesai":
        break

    # validasi nilai suhu
    try:
        suhu = float(input_suhu)

    except ValueError:
        print("Error: Suhu harus berupa angka.")
        continue


    skala_asal = input("Skala asal (C/F/K): ").strip().upper()

    skala_tujuan = input("Skala tujuan (C/F/K): ").strip().upper()


    try:
        hasil = konversi_suhu(suhu, skala_asal, skala_tujuan)
        print(f"Hasil: {suhu} {skala_asal} = {hasil} {skala_tujuan}")

    except ValueError as error:
        print(f"Error: {error}")