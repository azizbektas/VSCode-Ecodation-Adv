"""
   + Kart >> class adı. Özellikleri; ad, soyad, bankaAdi, para,   
       - BilgiVer fonk.
   + Atm >> class adı. Özellikleri;  ad, para
       - ParaCek, ParaYatir, BilgiVer, AyniMi fonk.
       - ParaCek >>
           - Farklı bir bankadan çekilecek ise %3 kesinti
       - ParaYatir >>
           - Farklı bir bankaya yatırılacak ise %3 kesinti
"""

class Kart:
    def __init__(self, ad, soyad, bankaAdi, para) -> None:
        self.ad = ad
        self.soyad = soyad
        self.bankaAdi = bankaAdi
        self.para = para
    
    def bilgiVer(self):
        return f"{self.ad} {self.soyad} {self.bankaAdi} {self.para}"

class Atm:
    def __init__(self, ad, para) -> None:
        self.ad = ad
        self.para = para
        
    def ayniMi(self, kart):
        if self.ad == kart.bankaAdi:
            return True
        else:
            return False

    def paraYatir(self, kart, miktar):
        kart.para += miktar
        self.para += miktar
        if not self.ayniMi(kart):
            kart.para -= miktar*0.03
            self.para += miktar*0.03
        # .... yatırıldı, ATM de ... TL. oldu
        print(f"{miktar} yatırıldı, ATM de {self.para} TL. oldu")

    def paraCek(self, kart, miktar):
        if self.para >= miktar:
            if kart.para >= miktar:
                kart.para -= miktar
                self.para -= miktar
                if not self.ayniMi(kart):
                    kart.para -= miktar*0.03
                    self.para += miktar*0.03
                    print(f"{miktar*0.03} TL. işlem ücreti alındı")
                print(f"{miktar} TL. çekildi. bakiyenizde {kart.para} kaldı")
            else:
                print(f"senin o kadar paran yok ki yok en fazla {kart.para} TL. çekebilirsin")
        else:
            # atm bu kadar para yok. en fazla {} TL. çekebilirsin
            print(f"atm bu kadar para yok en fazla {self.para} TL. çekebilirsin")

    def bilgiVer(self):
        return f"ATM : {self.ad} {self.para}"


k = Kart("Burak", "Günal", "halk", 500)
a = Atm("ziraat", 5000)
# a.paraYatir(k, 100)
a.paraCek(k, 100)
print(f"kart bilgileri {k.bilgiVer()}")
print(f"atm bilgileri {a.bilgiVer()}")