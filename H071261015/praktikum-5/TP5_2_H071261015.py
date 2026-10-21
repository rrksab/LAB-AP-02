alfabet = "abcdefghijklmnopqrstuvwxyz"

def cek_kata(teks, kata):
    indeks_kemunculan = []
    teks = teks.lower()
    kata = kata.lower()
    posisi = 0

    if kata == "":
        return indeks_kemunculan

    while True:
        indeks = teks.find(kata, posisi)
        
        if indeks == -1:
            break

        indeks_kemunculan.append(indeks)
        posisi = indeks + 1

    return indeks_kemunculan


def cek_batas_kata(teks, i, panjang):
    awal_kata = (i == 0 or teks[i - 1].lower() not in alfabet)

    akhir = i + panjang
    akhir_kata = (akhir == len(teks) or teks[akhir].lower() not in alfabet)

    return awal_kata and akhir_kata


def sensor_kata(teks, kata, simbol):
    if kata == "":
        return teks, 0, []

    indeks_kemunculan = cek_kata(teks, kata)
    indeks_valid = []

    for indeks in indeks_kemunculan:
        if cek_batas_kata(teks, indeks, len(kata)):
            indeks_valid.append(indeks)

    teks_sensor = ""
    posisi = 0
    jumlah_sensor = 0

    while posisi < len(teks):
        if posisi in indeks_valid:
            teks_sensor += simbol * len(kata)
            posisi += len(kata)
            jumlah_sensor += 1
        else:
            teks_sensor += teks[posisi]
            posisi += 1

    return teks_sensor, jumlah_sensor, indeks_valid

teks = input("Masukkan teks: ")
kata = input("Kata yang ingin disensor: ")
simbol = input("Masukkan simbol sensor: ")

hasil, jumlah, indeks = sensor_kata(teks, kata, simbol)

print("Teks tersensor:", hasil)
print("Jumlah kata disensor:", jumlah)
print("Indeks awal:", indeks)
