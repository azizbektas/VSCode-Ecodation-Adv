"""class Insan:
    ad = ""
    soyad = ""
    ozellik = []

i1= Insan()
i1.ad = "Ali"
i1.soyad = "Kemal"
i1.ozellik.append("kova")
i1.ozellik.append("uzun")

i2= Insan()
i2.ad = "Yusuf"
i2.ozellik.append("çok çalışkan")

i3= Insan()

print(f"{i1.ad} {i1.soyad} {i1.ozellik}")
print(f"{i2.ad} {i2.soyad} {i2.ozellik}")
print(f"{i3.ad} {i3.soyad} {i3.ozellik}")"""







"""class Insan:  
    insanSayisi = 0  
    def __init__(self) -> None:
        ad = ""
        soyad = ""
        self.ozellik=[]
        Insan.insanSayisi += 1
i1= Insan()
i1.ad = "Ali"
i1.soyad = "Kemal"
i1.ozellik.append("kova")
i1.ozellik.append("uzun")

i2= Insan()
i2.ad = "Yusuf"
i2.soyad = "Efe"
i2.ozellik.append("çok çalışkan")

i3= Insan()
i3.ad = "Elif"
i3.soyad = "Demirci"
print(f"{i1.ad} {i1.soyad} {i1.ozellik}")
print(f"{i2.ad} {i2.soyad} {i2.ozellik}")
print(f"{i3.ad} {i3.soyad} {i3.ozellik}")
print(Insan.insanSayisi)"""











"""
class Ogrenci:
    ogrenciSayisi = 0
    matematikSkorlari = 0
    def __init__(self,ad,soyad,matematikNotu) -> None:
        self.ad =ad
        self.soyad = soyad
        self.matematikNotu = matematikNotu
        Ogrenci.ogrenciSayisi += 1
        Ogrenci.matematikSkorlari += self.matematikNotu

o1 = Ogrenci("Ali", "Kemal", 80)
o1 = Ogrenci("Yusuf", "Efe", 90)
o1 = Ogrenci("Aziz", "Bektaş", 100)
print(f"matematik dersinin genel ortalaması {Ogrenci.matematikSkorlari/Ogrenci.ogrenciSayisi}")"""










# class Insan:  
#     insanSayisi = 0 
#     def __init__(self, ad, soyad, ozellik) -> None:
#         self.ad = ad
#         self.soyad = soyad
#         self.ozellik=ozellik
#         Insan.insanSayisi += 1

# i4 = Insan("ali","kemal", ["mavi gözlü","sarı saçlı"])
# print(i4.ad, i4.soyad, i4.ozellik, Insan.insanSayisi)




# class Customer:
#     def __init__(self, id, companyName, title="", address="") -> None:
#         self.id= id
#         self.companyName = companyName
#         self.title = title
#         self.address = address

# c1 = Customer("ALFKI", "Alfreds Futterkiste", "Sales Representative", "Obere Str. 57")
# c1.address= "Tuzla"
# c2 = Customer("BOLID", "B's Beverages")
# c2.id = "BLAUS"
# c2.companyName = "Blauer See Delikatessen"
# c2.title = "Owner"
# c2.address = "Berkeley Gardens 12 Brewery"
# print(f"{c1.id} {c1.companyName} {c1.title} {c1.address}")
# print(f"{c2.id} {c2.companyName} {c2.title} {c2.address}")






# def topla(a= 0, b= 0, c= 0):
#     return a+b+c

# result = topla()
# print(result)



# class SignOut:
#     def __init__(self, email, address="") -> None:
#         self.email = email
#         self.address = address


# newUser = SignOut("abc@email.com")
# newUser.address = "Tuzla/İstanbul"
# print(newUser.email, newUser.address)





class Ogrenci:
    def __init__(self, ad, soyad, vize, final) -> None:
        self.ad=ad
        self.soyad = soyad
        self.vize = vize
        self.final = final

    def ortalama(self):
        return float((self.vize+ self.final)/2)

    def yazdir(self):
        print(f"ortalama sonucu {self.ortalama()}")


o = Ogrenci("Ali", "Usta", 50, 60)
# print(o.ortalama())
o.yazdir()