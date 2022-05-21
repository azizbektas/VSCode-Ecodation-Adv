# class tiptir, user-defined tiptir
# Araba, Insan, Firma...


"""
class A1:
    pass

class A2():
    pass

class A3(object):
    pass
"""


from cgi import print_form


class Banka:
    bankaAdi = ""
    sahibi = ""
    subeSayisi = 1500


a = 10
# <class int>


class Insan:
    ad = ""
    soyad = ""


a = 19
"""i1 = Insan()
i1.ad = "Ali"
i1.soyad = "Kemal"
# print(i1)
# print(i1.ad, i1.soyad)

i2 = Insan()
i2.ad = "Mustafa"

i3 = Insan()
i3"""

"""print(i1.ad, i1.soyad)
print(i2.ad, i2.soyad)
print(i3.ad, i3.soyad)
"""


"""
Bisiklet Class
Attribute Ekle
Object Türet
Ekrana Print
Lütfen
"""


"""
class Bisiklet:
    marka = ""
    jant = 0
    renk = ""
    katlanirMi = True


b1 = Bisiklet()
b1.marka = "salcano"
b1.jant = 26
b1.renk = "sarı siyah"
b1.katlanirMi = False
if b1.katlanirMi:
    print(b1.marka, b1.jant, b1.renk, "Katlanabilir")
else:
    print(b1.marka, b1.jant, b1.renk, "Katlanamaz")
"""


"""class Ogrenci:
    adSoyad = ""
    not1 = 0
    not2 = 0


o1 = Ogrenci()
o1.adSoyad = input("ad soyad : ")
o1.not1 = int(input("not 1 : "))
o1.not2 = int(input("not 1 : "))
ort = (o1.not1 + o1.not2)/2
# ali kemal isimli öğrencinin not ortalaması ...
print(f"{o1.adSoyad} isimli öğrencinin not ortalaması {ort}")
"""

class Okul:
    kurumKodu = 0
    mudur = ""
    il = ""
    ilce = ""


o = Okul()
o.kurumKodu = 1001
o.mudur = "Ali Kemal"
o.ilce = "Tuzla"
o.il = "İstanbul"
print(f"Okulumuz {o.kurumKodu} kurum kodu ile {o.il} ili {o.ilce} ilçesinde faaliyet göstermektedir. Ben okul müdürü {o.mudur}")
