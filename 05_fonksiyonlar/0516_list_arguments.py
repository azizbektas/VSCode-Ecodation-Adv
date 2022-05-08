# region list_arguments_giris
"""
Argüman olarak → int, float, string,tuple, gönderebiliyorum, peki
Argüman olarak → list gönderebilir miyim? Cevabı, Evet
"""
# endregion

# region ornek
"""
def ortalama(liste):
    # print(type(liste))
    tekSayilarinToplami, tekSayilarinAdedi= 0,0
    for i in liste:
        if i%2==1:
            tekSayilarinAdedi += 1
            tekSayilarinToplami += i
    return f"listedeki {tekSayilarinAdedi} adet tek sayının toplamı {tekSayilarinToplami}"

print(ortalama([3,5,7,10,11,12])) 
"""

# endregion


from cgi import print_arguments
import time
# import datetime
from datetime import date, datetime
cTime = time.time()  #epoch time
# print(cTime)
#print(datetime.now()) #bugünün tarihi 2022-05-08 11:46:36.894214
#print(datetime.now().timestamp()) #epoch time
#print(datetime.fromisoformat("1998-07-29").timestamp()) #epoch time


def urunTarihKontrol(liste):
    # print(type(liste))
    for i in liste:
        cTime = time.time()
        pTime = datetime.fromisoformat(i).timestamp()
        # print(i, " " , pTime, "  ", cTime)
        # print((cTime-pTime)/86400)
        if round((cTime-pTime)/86400)>60:
            print(i)


urunTarihleri = [
    "2022-03-06",
    "2022-03-07",
    "2022-03-08",
    "2022-03-09",
    "2022-03-10",
]
urunTarihKontrol(urunTarihleri)