#sınıftaki notların ortalaması
d1,d2 = None, None
try:
    d1 = open("sinif_listesi.txt")
    d2 = open("not_listesi.txt")
    notlar = d2.readlines()
    ogrenciler = d1.readlines()
    # print(notlar)
    ortalama = []
    for oNotu in notlar:
        # print(oNotu.rstrip("\n"))
        n1, n2, p1, p2 = oNotu.rstrip("\n").split(",")
        ort = (int(n1)+int(n2)+int(p1)+int(p2))/4
        ortalama.append(ort)
    # print(ortalama)
    for i in range(len(ogrenciler)):
        oAdi = str(ogrenciler[i]).rstrip("\n")
        # 1. Öğrenci → Ali Ortalaması 45
        print(f"{i+1}. Öğrenci → {oAdi} Ortalaması {ortalama[i]}")
except Exception as e:
    raise e
finally:
    if d1 is not None:
        d1.close()
    if d2 is not None:
        d2.close()