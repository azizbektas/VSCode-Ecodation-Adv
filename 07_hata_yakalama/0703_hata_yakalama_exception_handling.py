# region hatalari_manuel_yakalama
"""
a = input("Sayı : ")
b = input("Sayı : ")
if a.isdigit() and b.isdigit():
    a, b = int(a), int(b)
    if b!=0:
        print(a/b)
    else:
        print("sayı 0 a bölünemez")
else:
    print("hatalı giriş")
"""
# endregion

# region try_except_formu
try:
    pass
except:  #tüm hataları yakalar
    pass
# endregion



"""try:
    a = int(input("Sayı : "))
    b = int(input("Sayı : "))
    print(a/b)
except:
    print("hatalı giriş")"""



"""
Exception Handling  →           try:
                                    {kodu çalıştırmak için bu bloktayım}
                                except:
                                    {exception var ise bu bloktayım}
                                else:
                                    {exception yok ise bu bloktayım}
                                finally:
                                    {mutlaka bu bloktayım}
""" 




"""
mevsimler = [
    "",
    "ilkbahar",
    "yaz",
    "sonbahar"
]
lütfen fav. mevsiminizi giriniz [1-4] : 1
ilkbahar

lütfen fav. mevsiminizi giriniz [1-4] : 5
lütfen [1-4] arası değer girin
"""