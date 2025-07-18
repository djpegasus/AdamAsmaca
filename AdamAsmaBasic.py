kelime = list("OTOBÜS")
tahmin_edilen =list("_") * len(kelime)
tahminler = []
hak = 6

print("ADAM ASMACA OYUNUNA HOŞGELDİNİZ...")
print(" ".join(tahmin_edilen))

while hak > 0 and "_" in tahmin_edilen:
    tahmin = input("Bir Harf Giriniz.. :").upper()
    
    if len(tahmin) > 1 or not tahmin.isalpha():
        print("Sadece 1 adet Harf Giriniz. :")
        continue
    
    if tahmin in tahminler:
        print("Aynı Harfi Daha Önce Kullandınız...")
        continue
    tahminler.append(tahmin)
    
    if tahmin in kelime:
        print("Doğru Tahmin Yaptınız !")
        for i in range(len(kelime)):
            if kelime[i] == tahmin:
                tahmin_edilen[i] = tahmin
    else:
        print("Hatalı Tahmin Yaptınız...")
        hak -= 1
        print(f"Kalan Hakkınız..{hak}")
    
    print(" ".join(tahmin_edilen))
    print(f"Kullanılan Harflar: {",".join(tahminler)}")

if "_" not in tahmin_edilen:
    print("Tebrikler Kelimeyi Buldunuz : ","".join(kelime))
    print(f"Kullanılan Harflar: {",".join(tahminler)}", f"Kalan Hakkınız {hak}")
else:
    print("Malesef Kaybettiniz. Olması Gereken Kelime : ","".join(kelime))
    print(f"Kullanılan Harflar: {",".join(tahminler)}", f"Kalan Hakkınız {hak}")