# region mode_x
# f = open("cihazlar.txt")
# f = open("cihazlar.txt", "r")
# f = open("cihazlar.txt", mode="r")
# x → mod dosya oluşturmak için kullanılır, kötü tarafı aynı dosya adı var ise KIZAR
# import os
# fName = input("oluşturulacak dosya adı : ")
# if fName in os.listdir():
#     print("hata, aynı dosya bu dizinde var")
# else:
#     f = open(fName, "x", encoding="utf-8")
#     print(f)
# endregion

# region mode_w
# w → yazma modu, eğer dizinde yok ise create edecek
'''with open("yazarlar.txt", "w", encoding="utf-8") as f:
    # print(f)
    # print(f.writable())
    f.write("Yaşar Kemal\n")
    f.write("Reşat Nuri Güntekin\n")
    #f.close() gerek yok, with içinden çıkınca silinecek
with open("yazarlar.txt", encoding="utf-8") as f:
    print(f.read(), end="")'''
# endregion


'''yazarlarListesi = []
while True:
    y = input("lütfen yazar adı ekleyin, çıkmak için [ç] : ")
    if y.lower()=="ç":
        break
    yazarlarListesi.append(y)
with open("yazarlar.txt", "w", encoding="utf-8") as f:
    for i in yazarlarListesi:
        #print(i)
        f.write(i+"\n")
with open("yazarlar.txt", encoding="utf-8") as f:
    print(f.read(), end="")
'''


# ödev → DRY sizde: DONT REPEAT YOURSELF
class FileOperation:
    def __init__(self, file) -> None:
        self.file = file

    def fileWrite(self):
        global yazarlarListesi
        with open(self.file , "w", encoding="utf-8") as f:
            for i in yazarlarListesi:
                f.write(i+"\n")

    def fileRead(self):
        with open(self.file , encoding="utf-8") as f:
            print(f.read(), end="")


yazarlarListesi = []
file = "yazarlar.txt"
while True:
    y = input("lütfen yazar adı ekleyin, çıkmak için [ç] : ")
    if y.lower() == "ç":
        break
    yazarlarListesi.append(y)


fObj = FileOperation(file)
fObj.fileWrite()
fObj.fileRead()
