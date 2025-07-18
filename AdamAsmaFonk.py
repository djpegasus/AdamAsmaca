kelime = list("OTOBÜS")
tahmin_edilen = list("_") * len(kelime)
tahminler= []

def adamAsmaca():
    hak = 6
    while hak > 0 and "_" in tahmin_edilen:
        tahmin = input("Bir Harf Tahmin Edininiz :").upper()
        
        if len(tahmin) > 1 or not tahmin.isalpha():
            print("Sadece 1 Adet Harf Giriniz.")
            continue
        if tahmin in tahminler:
            print("Daha Önce Bu Harfi Tahmin Ettiniz")
            continue
        tahminler.append(tahmin)
        
        if tahmin in kelime:
            print("Doğru Harf Tahmin Ettiniz :) ")
            for i in range(len(kelime)):
                if kelime[i] == tahmin:
                    tahmin_edilen[i] = tahmin
        else:
            print("Hatalı Tahmin Ettiniz...")
            hak -= 1
            print(f"Kalan Hakkınız...{hak}")
        print(" ".join(tahmin_edilen))
        print(f"Kullandığınız Kelimeler : {",".join(tahminler)}")
    
    if "_" not in tahmin_edilen:
        print("Tebrikler Kelimeyi Bildiniz","".join(kelime))
        print(f"Kullanılan Harflar: {",".join(tahminler)}", f"Kalan Hakkınız: {hak}")
    else:
        print("Malesef Kelimeyi Bilemediniz. Bulmanız Gereken Kelime :","".join(kelime))
        print(f"Kullanılan Harflar: {",".join(tahminler)}", f"Kalan Hakkınız: {hak}")

print("ADAM ASMACA OYUNUNA HOŞ GELDİNİZ...")
print(" ".join(tahmin_edilen))

adamAsmaca()