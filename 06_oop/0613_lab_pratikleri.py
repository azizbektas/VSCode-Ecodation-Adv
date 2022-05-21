"""
   - Mesajlaşma programı yapalım;
   - User class >> ad, soyad, mesaj
       + public >> ad, soyad
       + private >> mesaj
       + mesaj >> set edilirken, TR karakterler ing. olacak
       - SendMessage(user, mesaj)   hangi usera, ne mesajı
       - SendMessage Çıktı; ..... ..... >> ..... ..... kişisine ..... mesajı gönderildi
   Örn;
   u1 = User("ali1", "veli1", "mesaj içeriği")
   u2= User("ali2", "veli2", "mesaj içeriği")
   mesaj içeriği > mesaj icerigi şeklinde tr karakterleri değiştireceğiz
"""


class User:
    trSozluk = {
        "ç": "c",
        "ğ": "g",
        "ı": "i",
        "ö": "o",
        "ş": "s",
        "ü": "u"
    }

    def __init__(self, ad, soyad) -> None:
        self.ad = ad
        self.soyad = soyad

    @property
    def mesaj(self):
        """The mesaj property."""
        return self._mesaj

    @mesaj.setter
    def mesaj(self, value):
        self._mesaj = ""
        for i in value:
            if i in User.trSozluk.keys():
                self._mesaj += User.trSozluk[i]
            else:
                self._mesaj += i
        if len(str(self._mesaj)) > 30:
            self._mesaj = self._mesaj[0:30] + "..."

    def SendMessage(self, user, mesaj):
        self.user = user
        self.mesaj = mesaj
        print(
            f"{self.ad} {self.soyad} >> {user.ad} {user.soyad} kişisine {self.mesaj} mesajı gönderildi")


u1 = User("Aziz", "Bektaş")
u2 = User("Burak", "Günal")
# u1.SendMessage(u2, "Merhaba, Nasılsın?")
u1.mesaj = "buradan daburadan da buradan da buradan da buradan daşşşşşşşşşşşçççç"
u1.SendMessage(u1, u1.mesaj)
