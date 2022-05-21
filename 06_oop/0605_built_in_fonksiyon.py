class Calisan:
    def __init__(self, ad, soyad, tc, maas) -> None:
        self.ad = ad
        self.soyad = soyad
        self.tc = tc
        self.maas = maas

    def bilgiVer(self):
        return f"{self.ad} {self.soyad} {self.tc} {self.maas}"

    def zamYap(self,miktar):
        if miktar>self.maas/2:
            cvp= input("Maasın yarısın fazla zam yapılıyor.  Emin misin? E/H: ")
            if cvp.lower() == "e":
                self.maas += miktar
                print(f"Yeni maas: {self.maas}")
            else:
                print("Peki, yanlışlıkla girildi.")
        else:
            self.maas += miktar
            print(f"Yeni maas: {self.maas}")


c1 = Calisan("Elif", "Demirci", "1549599", 6000)
# print(c1.bilgiVer())
# c1.zamYap(5000)
# print(c1.bilgiVer()

# region bulint-in-fonk
# getattr
# hasattr
# setattr
# print(getattr(c1, "ad"))
# setattr(c1, "ad", "Aziz")
# print(c1.bilgiVer())
# print(hasattr(c1, "ad"))
# print(hasattr(c1, "name"))
# endregion


# region bulint-in-attribute
"""
__doc
__dic
__module
__name
"""
# print(c1.__doc__)
# print(c1.__dict__)
# calisan = c1.__dict__
# print(calisan)
# for key, value in calisan.items():
#     print(key, value)
print(c1.__module__)
# print(c1.__name__)
# endregion