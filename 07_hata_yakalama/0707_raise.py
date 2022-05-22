# hata yükseltmek → raise the error
# region raise-giris
"""x = -1
if x<0:
    raise Exception("Lütfen, Negatif Değer Girmeyin")"""
# endregion

"""
"""


"""def degerAl():
    x = -1
    if x < 0:
        raise ValueError("Lütfen, Negatif Değer Girmeyin")

try:
    degerAl()
except ValueError as e:
    print(e)
"""


"""
Kullanıcıdan D.Günü Girmesini İsteyelim
Ancak ısrarla bugünün tarihinden büyük bir tarih girmeye çalışsın
Nazikçe uyaralım, d.Gününü bugüne set edelim
"""




'''import datetime
def degerAl():
    global dTarihi
    dTarihi = input("y-a-g : ")  # 1980-01-06
    bugunEpoch = datetime.datetime.now().timestamp()
    dTarihiEpoch = datetime.datetime.fromisoformat(dTarihi).timestamp()
    if dTarihiEpoch > bugunEpoch:
        raise Exception("d.Tarihi Bugünün Tarihinden Büyük Olamaz")


try:
    degerAl()
except Exception as e:
    dTarihi = datetime.datetime.now()
    print(e, "d.Tarihi", dTarihi, "olarak set edildi")'''


# ödev
# kullanıcıya doğru formatta tarih girmesini isteyin ValueError Yönet Lütfen


# ödev
"""
100'e kadar sayı giriniz: 
110 → 110 izin verilen aralık dışında
70 → 70 izin verilen aralıkta
"""
try:
    x = int(input("100'e kadar sayı giriniz: "))
    if x > 100:
        raise ValueError(x)
except ValueError:
    print(f"{x} izin verilen aralık dışında")
else:
    print(f"{x} izin verilen aralıkta")

