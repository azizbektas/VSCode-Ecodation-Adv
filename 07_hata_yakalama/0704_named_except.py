# region hata_test
"""
a = int(input("Sayı : "))
b = int(input("Sayı : "))
print(a/b)
------
mevsimler = [
    "",
    "ilkbahar",
    "yaz",
    "sonbahar",
    "kış"
]
fav = int(input("Lütfen favori mevsimini giriniz:  [1 - 4] : "))
print(mevsimler[fav])
----
from selenium import webdriver
"""
# endregion

# region named_except
"""
try:
    a = int(input("Sayı : "))
    b = int(input("Sayı : "))
    print(a/b)
except ValueError:
    print("Int'e Çevirirken Hata Oluştu")
except ZeroDivisionError:
    print("Sayı 0'a Bölünemez")
"""
# endregion

# region catch-all-except-clause
"""try:
    a = int(input("Sayı : "))
    b = int(input("Sayı : "))
    print(a/b)
except ValueError:
    print("Int'e Çevirirken Hata Oluştu")
except ZeroDivisionError:
    print("Sayı 0'a Bölünemez")
except: #catch-all except clause
    print("Kalan Tüm Hatalar")"""

# endregion

"""
try:
    a = int(input("Sayı : "))
    b = int(input("Sayı : "))
    print(a/b)
except: #catch-all except clause
    print("Kalan Tüm Hatalar")
except ValueError:
    print("Int'e Çevirirken Hata Oluştu")
except ZeroDivisionError:
    print("Sayı 0'a Bölünemez")"""


"""try:
    a = int(input("Sayı : "))
    b = int(input("Sayı : "))
    print(a/b)
except (ValueError, ZeroDivisionError):
    print("Kullanıcı Girişi Hatası")
except:  # catch-all except clause
    print("Kalan Tüm Hatalar")"""


mevsimler = [
    "",
    "ilkbahar",
    "yaz",
    "sonbahar",
    "kış"]

try:
    fav = int(input("Lütfen favori mevsimini giriniz:  [1 - 4] : " ))
    print(mevsimler[fav])
except IndexError as e:
    print(e, "Lütfen 1 ile 4 arasında değer giriniz")
