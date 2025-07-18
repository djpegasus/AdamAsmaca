from random import choice

def kelimeDosya():
    with open("words.wrd", "r", encoding="utf-8") as file:
        secilen = file.read().splitlines()
        seclist =[]
        for i in secilen:
            seclist.append(i)
        seckelime = choice(seclist)
    return seckelime

def adamAsma(self):
    hak = 6
    while hak > 0 and "_" in tahmin_edilen:
        tahmin = input("Bir Harf Tahmin Ediniz :").upper()
        
        if len(tahmin) > 1 or not tahmin.isalpha():
            print("Lütfen Bir Adet Harf Tahmin Ediniz...")
            continue
        if tahmin in tahminler:
            print("Aynı Harfi Daha Önce Kullandınız...")
            continue
        tahminler.append(tahmin)
        
        if tahmin in kelime:
            print("DOĞRU TAHMİN !")
            for i in range(len(kelime)):
                if kelime[i] == tahmin:
                    tahmin_edilen[i] = tahmin
        else:
            print("HATALI TAHMİN :(")
            hak -= 1
            print(f"Kalan Hakkınız : {hak}")
            
        print(" ".join(tahmin_edilen))
        print(f"Kullanılan Harfler :{",".join(tahminler)}", f"Kalan Haklar : {hak}")

kelime = kelimeDosya()
tahmin_edilen = list("_") * len(kelime)
tahminler = []
print("ADAM ASMACA OYUNUNA HOŞ GELDİNİZ...")
print(" ".join(tahmin_edilen), f"Kelime : {kelime}" )
adamAsma(kelime)

if "_" not in tahmin_edilen:
    print(f"Tebrikler Kelimeyi Bildiniz : {kelime}")
else:
    print(f"Malesef Kelimeyi Bilemediniz. Kelimemiz : {kelime}")