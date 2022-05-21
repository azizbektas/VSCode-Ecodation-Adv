# region ilkpratif
# a = 10
# class Urun:
#     def __init__(self, urunId, ad, fiyat) -> None:
#         self.urunId = urunId
#         self.ad = ad
#         self.fiyat = fiyat

#     def __str__(self) -> str:
#         return f"""
#         Ürüne Ait Bilgileri:
#         Urun Id         : {self.urunId}
#         Urun Adı        : {self.ad}
#         Urun Fiyat      : {self.fiyat}
#         """

# u1=Urun(1, "Çay", 16.99)
# print(u1)
# endregion

class Aday:
    def __init__(self, no, adSoyad, rol, mNot, uNot) -> None:
        self.no = no
        self.adSoyad = adSoyad
        self.rol=rol
        self.modulNotOrtalamasi = mNot
        self.uygulamaNotOrtalamasi = uNot

    @property
    def rol(self):
        """The rol property."""
        return self._rol

    @rol.setter
    def rol(self, value):
        self._rol = value

    @property
    def no(self):
        """The no property."""
        return self._no

    @no.setter
    def no(self, value):
        self._no = value

    @property
    def adSoyad(self):
        """The adSoyad property."""
        return self._adSoyad

    @adSoyad.setter
    def adSoyad(self, value):
        self._adSoyad = value

    @property
    def modulNotOrtalamasi(self):
        """The modulNotOrtalamasi property."""
        return self._modulNotOrtalamasi

    @modulNotOrtalamasi.setter
    def modulNotOrtalamasi(self, value):
        self._modulNotOrtalamasi = value

    @property
    def uygulamaNotOrtalamasi(self):
        """The uygulamaNotOrtalamasi property."""
        return self._uygulamaNotOrtalamasi

    @uygulamaNotOrtalamasi.setter
    def uygulamaNotOrtalamasi(self, value):
        self._uygulamaNotOrtalamasi = value

    @property
    def notHesapla(self):
        """The foo property."""
        return (self.modulNotOrtalamasi+self.uygulamaNotOrtalamasi)/2

class Ogrenci(Aday):
    def __init__(self, no, adSoyad, rol,mNot, uNot) -> None:
        super().__init__(no, adSoyad,rol, mNot, uNot)

    def notHesapla(self):
        if super().notHesapla < 70:
            return -1
        return 0

    def __str__(self) -> str:
        durum = ""
        if self.notHesapla() == -1:
            durum = "BAŞARISIZ"
        else:
            durum = "BAŞARILI"
        return f"{self.adSoyad} Ortalaman {super().notHesapla} Sonuç {durum}"

class Ogretmen(Aday):
    def __init__(self, no, adSoyad,rol, mNot, uNot) -> None:
        super().__init__(no, adSoyad, rol,mNot, uNot)

    def notHesapla(self):
        if super().notHesapla < 80:
            return -1
        return 0

    def __str__(self) -> str:
        durum = ""
        if self.notHesapla() == -1:
            durum = "BAŞARISIZ"
        else:
            durum = "BAŞARILI"
        return f"{super().rol} Rolündeki {self.adSoyad} Ortalaman {super().notHesapla} Sonuç {durum}"

# Ogretmen Rolündeki Aziz Bektaş  Ortalaman 80.0 Sonuç BAŞARILI
# ogrenci1 = Ogrenci(1001, "Aziz Bektaş", 70, 80)
# print(ogrenci1)
o = Ogretmen(101, "burak günal", "Öğretmen", 70, 90)
print(o)
