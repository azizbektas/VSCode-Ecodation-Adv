'''# class Sistem:
#     def __init__(self) -> None:
#         self.__ad = "windows"

#     @property
#     def ad(self):
#         return self.__ad


# s = Sistem()
# # s.ad = "linux" # AttributeError: can't set attribute 'ad'
# print(s.ad)


class Uye:
    @property
    def dTarihi(self):
        """The dTarihi property."""
        return self._dTarihi

    @dTarihi.setter
    def dTarihi(self, value):
        if value > 2022:
            self._dTarihi = 2022
        else:
            self._dTarihi = value


u = Uye()
u.dTarihi = 2030
print(u.dTarihi)


class Araba:
    @property
    def motor(self):
        """The motor property."""
        return self._motor

    @motor.setter
    def motor(self, value):
        self._motor = value

    @property
    def sasi(self):
        """The sasi property."""
        return self._sasi

    @sasi.setter
    def sasi(self, value):
        self._sasi = value


# import datetime
# result = datetime.datetime.now().hour
# print(result)
'''

'''
class Hotel:
    @property
    def ad(self):
        """The ad property."""
        return self._ad

    @ad.setter
    def ad(self, value):
        self._ad = value

    @property
    def yildiz(self):
        """The yildiz property."""
        return self._yildiz

    @yildiz.setter
    def yildiz(self, value):
        self._yildiz = value

    def __str__(self) -> str:
        return f"hotelimizin adı {self.ad} siz değerli müşterilerimizi {self.yildiz} yıldızlı hotelimizde ...."

h = Hotel()
h.ad = "Titanik"
h.yildiz = 5
print(h)
'''
'''

class Sirket:
    @property
    def ad(self):
        """The ad property."""
        return self._ad

    @ad.setter
    def ad(self, value):
        self._ad = value

    @property
    def ceo(self):
        """The ceo property."""
        return self._ceo

    @ceo.setter
    def ceo(self, value):
        self._ceo = value

    @property
    def kurulusYil(self):
        """The kurululYil property."""
        return self._kurulusYil

    @kurulusYil.setter
    def kurulusYil(self, value):
        self._kurulusYil = value

    @property
    def merkezi(self):
        """The merkezi property."""
        return self._merkezi

    @merkezi.setter
    def merkezi(self, value):
        self._merkezi = value

    # netflix şifketi 1997 yılında Reed Hastings tarafından Kalifornia'da kuruldu
    def yaz(self):
        print(f"{self.kurulusYil} yılında {self.ceo} tarafından {self.merkezi}'da kuruldu")


s = Sirket()
s.ad = "netflix"
s.kurulusYil = 1997
s.ceo = "Reed Hastings"
s.merkezi = "Kalifornia"
s.yaz()'''


'''class Top:
    def __init__(self, marka, numara,  fiyat) -> None:
        self.marka = marka
        self.numara = numara
        self.fiyat = fiyat

    @property
    def numara(self):
        """The numara property."""
        return self._numara

    @numara.setter
    def numara(self, value):
        if 3 <= value <= 5:
            self._numara = value
        else:
            self._numara = -1

    @property
    def marka(self):
        """The marka property."""
        return self._marka

    @marka.setter
    def marka(self, value):
        self._marka = value

    @property
    def fiyat(self):
        """The fiyat property."""
        return self._fiyat

    @fiyat.setter
    def fiyat(self, value):
        self._fiyat = value

    def __str__(self) -> str:
        if self.numara == -1:
            return f"mağazamızda böyle bir numara yoktur"
        return f"{self.marka} marka {self.numara} numaralı topumuzuuun fiyatı {self.fiyat}"


t = Top("adi",1, 100)
# t.marka = "adidas"
# t.numara = 2
# t.fiyat = 400
print(t)
'''


class Device:
    def __init__(self, dType, ip, port, username, password) -> None:
        self.dType = dType
        self.port = port
        self.ip = ip
        self.username = username
        self.password = password

    @property
    def dType(self):
        """The dType property."""
        return self._dType

    @dType.setter
    def dType(self, value):
        self._dType = value

    @property
    def ip(self):
        """The ip property."""
        return self._ip

    @ip.setter
    def ip(self, value):
        self._ip = value

        @property
        def port(self):
            """The port property."""
            return self._port

        @port.setter
        def port(self, value):
            self._port = value

    @property
    def username(self):
        """The username property."""
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def password(self):
        """The password property."""
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    def __str__(self) -> str:
        return f"cihaz tipi {self.dType} olan {self.ip} IP adresli cihaz {self.port}. portu dinliyor. kullanıcı adı {self.username} parola {self.password}"


d = Device("cisco_ios", "172.12.0.1", 22, "admin", "admin")
print(d)
