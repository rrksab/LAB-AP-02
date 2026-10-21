
def bersihkan_teks(teks):
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    hasil = ""  

    for karakter in teks:
        karakter = karakter.lower() 

        if karakter in alfabet:
            hasil += karakter

    return hasil

                                                                                   
def cek_palinrome(teks):
    terbalik = "".join(reversed(teks))

    if teks == terbalik:
        return True, -1

    else:
        return False



def inti_palinrome(teks):
    teks_bersih = bersihkan_teks(teks)
    palindrom_terbaik = ""
    indeks_awal = 0

    for i in range(len(teks_bersih)):
        for j in range(i + 1, len(teks_bersih) + 1):
            potongan = teks_bersih[i:j]
            hasil_cek = cek_palinrome(potongan)

            if hasil_cek and len(potongan) > len(palindrom_terbaik):
                palindrom_terbaik = potongan
                indeks_awal = i

    return {"teks": palindrom_terbaik,"panjang": len(palindrom_terbaik),"indeks_awal": indeks_awal}

teks = input("Masukkan teks prasasti: ")

print("Teks bersih:", bersihkan_teks(teks))
print("Output Terharap:", inti_palinrome(teks))

