# region fonksiyon_turu_2_parametre_alan_deger_dondurmeyen
"""
Fonksiyon tanımlama anında argüman alır, değer döndürmez
"""
# endregion

# region ornek1
"""
def yas(dTarihi):
    print(f"Yaşınız, {2021-dTarihi}")

yas(int(input("lütfen d.tarihi giriniz: ")))
"""
# endregion

# region ornek2
def tekcift(s):
    if str(s).isdigit():
        s=int(s)
        if s%2==0:
            print(f"{s } çift")
        else:
            print(f"{s } tek")
    else:
        print("lutfen sayi giriniz")

listem = [3, 6, 45, 98, 66, 45 , 65]
for i in listem:
    tekcift(i)
# endregion
