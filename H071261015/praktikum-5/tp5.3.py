
ALFABET = "abcdefghijklmnopqrstuvwxyz"


def cek_sandi(ch, k):
    huruf = ch.lower()
    posisi = ALFABET.find(huruf)

    if posisi == -1:
        return ch

    hasil = ALFABET[(posisi + k) % 26]

    if ch.isupper():
        return hasil.upper()

    return hasil


def mesin_enkripsi(teks, k):
    hasil = ""

    for ch in teks:
        hasil += cek_sandi(ch, k)

    return hasil


def mesin_dekripsi(teks, k):
    return mesin_enkripsi(teks, -k)


def retas_sandi(sandi, kata_kunci):
    hasil = []

    if not kata_kunci or not kata_kunci.strip():
        return hasil

    for kunci in range(26):
        pesan_asli = mesin_dekripsi(sandi, kunci)

        if kata_kunci.casefold() in pesan_asli.casefold():
            hasil.append((kunci, pesan_asli))

    return hasil


def main():
    sandi = input("Masukkan pesan tersita (enkripsi Caesar): ")
    kata_kunci = input("Masukkan kata kunci target: ")

    if not sandi.strip() or not kata_kunci.strip():
        print("Output Deskripsi: []")
        return

    hasil = retas_sandi(sandi, kata_kunci)
    print("Output Deskripsi:", hasil)

if __name__ == "__main__":
    main()