"""
   - Araba class-> ad, motor, yas, model, ivme, maxHiz, hiz
       Hızlan() -> maxHiza kadar, ivme değerinde hız artışı
       Yavasla() -> 0a kadar, ivme değerinde azalışı

   - Audi class -> otoPark
   - Mercedes class -> guvenlik
"""

class Araba:
    def __init__(self, ad, motor, yas, model, ivme, maxHiz, hiz) -> None:
        self.ad = ad
        self.motor = motor
        self.yas = yas
        self.model = model
        self.ivme = ivme
        self.maxHiz = maxHiz
        self.hiz = hiz

    def Hizlan(self):
        self.hiz += self.ivme
        if self.hiz>180:
            print("emin misin ceza alabilirsin, biraz yavaşla lütfen")
        if self.hiz>self.maxHiz:
            self.hiz = self.maxHiz
        print(self.hiz)

    def Yavasla(self):
        if self.hiz>0:
            self.hiz -= self.ivme
            if self.hiz<0:
                self.hiz=0
            print(self.hiz)
        else:
            print("zaten duruyorsun ayağını frenden çek :-)")

    # def __str__(self) -> str:
    #     return f"{self.ad} motor hacmi {self.motor}, {self.yas} yaşında,  {self.model} modeli her hızlanma da {self.ivme} km. ivme ile hızlanırım {self.maxHiz} km. hıza çıkabilirim, anlık hızım {self.hiz}"

    def bilgiVer(self):
        return f"{self.ad} motor hacmi {self.motor}, {self.yas} yaşında,  {self.model} modeli her hızlanma da {self.ivme} km. ivme ile hızlanırım {self.maxHiz} km. hıza çıkabilirim, anlık hızım {self.hiz}"

      
class Audi(Araba):
    def __init__(self, ad, motor, yas, model, ivme, maxHiz, hiz, otopark) -> None:
        super().__init__(ad, motor, yas, model, ivme, maxHiz, hiz)
        self.otopark = otopark

class Mersedes(Araba):
    def __init__(self, ad, motor, yas, model, ivme, maxHiz, hiz, guvenlik) -> None:
        super().__init__(ad, motor, yas, model, ivme, maxHiz, hiz)
        self.guvenlik = guvenlik


au1 = Audi("a5", 2, 5, "A5 Sportback 2.0", 5, 200,150,"Otopark Sensörü")
# au1.Yavasla()
# au1.Yavasla()
# au1.Yavasla()
au1.Hizlan()
au1.Hizlan()
au1.Hizlan()
au1.Hizlan()
print(au1)
print(au1.bilgiVer())
