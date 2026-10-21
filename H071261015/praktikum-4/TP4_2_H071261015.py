def hitung_statistik(*args):

    if len(args) == 0:
        return None, None, None

    rata_rata = sum(args) / len(args)
    nilai_tertinggi = max(args)
    nilai_terendah = min(args)

    return rata_rata, nilai_tertinggi, nilai_terendah

nilai_siswa = []

while True:
    input_nilai = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ").strip()

    # input kosong = selesai
    if input_nilai == "":
        break

    try:
        nilai = float(input_nilai)

        # validasi nilai ujian
        if nilai < 0 or nilai > 100:
            print("Nilai harus berada antara 0 dan 100.")
            continue

        nilai_siswa.append(nilai)

    except ValueError:
        print("Input nilai harus berupa angka.")


# jika tidak ada data
if len(nilai_siswa) == 0:
    print("Data nilai tidak tersedia.")

else:
    rata_rata, nilai_tertinggi, nilai_terendah = hitung_statistik(*nilai_siswa)

    print(f"Rata-rata kelas: {rata_rata}")
    print(f"Nilai tertinggi: {int(nilai_tertinggi) if nilai_tertinggi.is_integer() else nilai_tertinggi}")
    print(f"Nilai terendah: {int(nilai_terendah) if nilai_terendah.is_integer() else nilai_terendah}")


