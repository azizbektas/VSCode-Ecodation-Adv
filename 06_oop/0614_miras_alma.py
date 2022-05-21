'''# miras alma → inheritance
# kalıtım
# class Timsah:
#     pass

# class Aslan:
#     pass

# class Papagan:
#     pass


# ad = "burak"


class Insan:
    #pass   ad, soyad, dTarihi

    @property
    def ad(self):
        """The ad property."""
        return self._ad

    @ad.setter
    def ad(self, value):
        self._ad = value

    @property
    def soyad(self):
        """The soyad property."""
        return self._soyad

    @soyad.setter
    def soyad(self, value):
        self._soyad = value

    @property
    def dTarihi(self):
        """The dTArihi property."""
        return self._darihi

    @dTarihi.setter
    def dTarihi(self, value):
        self._dTarihi = value

class Ogrenci(Insan):
    # pass Vize,Final, OkulNo

    @property
    def vize(self):
        """The vize property."""
        return self._vize
    @vize.setter
    def vize(self, value):
        self._vize = value

    @property
    def final(self):
        """The final property."""
        return self._final
    @final.setter
    def final(self, value):
        self._final = value

    @property
    def okulNo(self):
        """The okulNo property."""
        return self._okulNo
    @okulNo.setter
    def okulNo(self, value):
        self._okulNo = value

class Memur(Insan):
    # pass, SicilNo, İseGirisTarihi, Maas, Derece, Kademe
    @property
    def sicilNo(self):
        """The sicilNo property."""
        return self._sicilNo
    @sicilNo.setter
    def sicilNo(self, value):
        self._sicilNo = value

    @property
    def iseGirisTarihi(self):
        """The iseGirisTarihi property."""
        return self._iseGirisTarihi
    @iseGirisTarihi.setter
    def iseGirisTarihi(self, value):
        self._iseGirisTarihi = value

    @property
    def maas(self):
        """The maas property."""
        return self._maas
    @maas.setter
    def maas(self, value):
        self._maas = value
    @property
    def derece(self):
        """The derece property."""
        return self._derece
    @derece.setter
    def derece(self, value):
        self._derece = value
    @property
    def kademe(self):
        """The kademe property."""
        return self._kademe
    @kademe.setter
    def kademe(self, value):
        self._kademe = value

class Ogretmen(Memur):
    @property
    def brans(self):
        """The brans property."""
        return self._brans
    @brans.setter
    def brans(self, value):
        self._brans = value
    @property
    def haftalikDersSaati(self):
        """The haftalikDersSaati property."""
        return self._haftalikDersSaati
    @haftalikDersSaati.setter
    def haftalikDersSaati(self, value):
        self._haftalikDersSaati = value
    @property
    def rehberlikSinifi(self):
        """The rehberlikSinifi property."""
        return self._rehberlikSinifi
    @rehberlikSinifi.setter
    def rehberlikSinifi(self, value):
        self._rehberlikSinifi = value



i1= Insan()
o1=Ogrenci()
o1.ad = "burak"
m = Memur()
ogrt = Ogretmen()
result = issubclass(Ogrenci, Insan)
result = isinstance(ogrt, Ogretmen)
print(result)
'''


'''class Super:
    def __init__(self, ad) -> None:
        self.ad = ad

    def __str__(self) -> str:
        return f"benim adım {self.ad}"

class Sub(Super):
    def __init__(self, ad) -> None:
        super().__init__(ad)


s = Sub("Aziz")
print(s)'''

#futbol oyunu 11 kişi ile oynanır, hakem sayisi 1 dir
class Spor:
    def __init__(self, ad, oyuncuSayisi, hakemSayisi) -> None:
        self.ad = ad
        self.oyuncuSayisi = oyuncuSayisi
        self.hakemSayisi = hakemSayisi
        
    def __str__(self) -> str:
        return f"{self.ad} oyunu {self.oyuncuSayisi} kişi ile oynanır, hakem sayısı {self.hakemSayisi}"

class Futbol(Spor):
    def __init__(self, ad, oyuncuSayisi, hakemSayisi) -> None:
        super().__init__(ad, oyuncuSayisi, hakemSayisi)


class Basketbol(Spor):
    def __init__(self, ad, oyuncuSayisi,hakemSayisi) -> None:
        super().__init__(ad, oyuncuSayisi,hakemSayisi)


f = Futbol("futbol",11,1)
b = Basketbol("basketbol",5, 3)
print(f)
print(b)
