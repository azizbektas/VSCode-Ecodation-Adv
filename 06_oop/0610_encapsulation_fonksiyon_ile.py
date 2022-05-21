class Ogrenci:
    def __init__(self, ad, soyad, tc, sinif, okul) -> None:
        self.ad = ad
        self.soyad = soyad
        self.tc = tc
        # self.__sinif = sinif
        # self.__okul = okul
        self.setSinif(sinif)
        self.setOkul(okul)

    def setOkul(self, arg):
        if arg=="Tuzla Meslek Lisesi":
            self.__okul = arg
        else:
            self.__okul = -1

    def getOkul(self):
        return self.__okul

    def setSinif(self, arg):
        if 8<arg<13:
            self.__sinif = arg
        else:
            self.__sinif = -1

    def getSinif(self):
        return self.__sinif

    def __str__(self) -> str:
        if self.getSinif()==-1:
            return f"üzgünüm!!! sınıf düzeyi [9-12] dışında kabul edilemez"
        if self.getOkul()==-1:
            return f"üzgünüm!!! Tuzla dışından kayıt kabul edilemez"
        return f"{self.ad} {self.soyad} {self.tc} {self.__sinif}  {self.__okul}"

o1 = Ogrenci("yusuf", "efe", 1111111,9, "Tuzla Meslek Lisesi")
# o1.sinif = "1-B"
# o1.setSinif(11)
# o1.setOkul("Tuzla Meslek Lisesiiiiii")
# print(o1.getSinif())
# if o1.sinif != "1-B":
#     print("bu sınıfta olmamalısın")
print(o1)





