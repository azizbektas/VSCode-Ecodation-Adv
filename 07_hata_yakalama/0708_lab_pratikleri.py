# region lab-pratigi-1-parola-politikası
""""
tr karakter girilmesin
min 8 karakter uzunluğunda olsun
"""
"""while True:
    trKarakterler = ["ş", "ç", "ğ", "ü", "ö", "ı", "İ"]
    p = input("parola politikası test et, çıkmak için [ç] : ")
    if p.lower() == "ç":
        break
    try:
        if len(p) < 8:
            raise Exception(
                "uygun olmayan parola - minimum karakter politikası")
        for i in p:
            if i in trKarakterler:
                raise Exception(
                    "uygun olmayan parola - tr karakter politikası")
        print("uygun parola")
    except Exception as e:
        print(e)"""

# DRY pratiği ile
'''
trKarakterler = ["ş", "ç", "ğ", "ü", "ö", "ı", "İ"]


class CheckPassword:
    def __init__(self, password) -> None:
        self.password = password

    def isValidPassword(self):
        try:
            if len(self.password) < 8:
                raise Exception(
                    "uygun olmayan parola - minimum karakter politikası")
            for i in self.password:
                if i in trKarakterler:
                    raise Exception(
                        "uygun olmayan parola - tr karakter politikası")
            print("uygun parola")
        except Exception as e:
            print(e)


testPassword = input("lütfen test için parola giriniz: ")
c = CheckPassword(testPassword)
c.isValidPassword()

'''
# endregion


# region lab-pratigi-1-parola-politikası
"""
kullanıcıdan fav. gezegenini alalım, gezegen listesinde yok ise hata versin
"""
# endregion


def gAra(g):
    gezegenler = [
        "merkür",
        "venüs",
        "dünya",
        "mars",
        "jüpiter",
        "satürn",
        "uranüs",
        "neptün"
    ]
    if not isinstance(g, str):
        raise TypeError("gezegen adı hata, str tipinde olmalı")
    # if type(g) is not str:
    #     raise TypeError("gezegen adı hata, str tipinde olmalı")
    if g not in gezegenler:
        raise ValueError(f"gezegen adı hata, {g} gezegen ismi değildir")
    print(f"girdiğiniz fav gezeneniniz {g}")


try:
    gAra(3)
except(TypeError, ValueError) as e:
    print(e)