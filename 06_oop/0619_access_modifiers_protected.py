class Calisan:
    def __init__(self, adSoyad, maas):
        self.adSoyad = adSoyad
        self.maas = maas
        self._prim = 0

    @property
    def maas(self):
        """The maas property."""
        return self._maas

    @maas.setter
    def maas(self, value):
        self._maas = value

    def __str__(self):
        return f"Çalışan {self.adSoyad} adlı kişinin maaşı {self.maas}"


class AyinElemani(Calisan):
    def __init__(self, calisan, prim):
        self.calisan = calisan
        self._prim = prim

    def __str__(self):
        return f"{self.calisan.adSoyad} isimli elemanın Bu ayki maaşı {self.calisan.maas + self._prim}"


c = Calisan("Aziz Bektaş", 1000)
# print(c.maas)
eleman = AyinElemani(c, 500)
print(eleman)
