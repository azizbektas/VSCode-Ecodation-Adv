'''with open("cihazlar.txt", "a", encoding="utf-8") as f:
    f.write("10→wmware esxi\n")'''


'''with open("cihazlar.txt",encoding="utf-8") as f:
    print(f.read())'''


# end yalın güncelleme pratiği
with open("cihazlar.txt", "r+", encoding="utf-8") as f:
    cihazListesi = f.readlines()
    # print(cihazListesi)
    cihazListesi.insert(1, "4→router\n")
    # print(cihazListesi)
    # print(f.tell())
    f.seek(0)
    f.writelines(cihazListesi)  # 1.yöntem
    # for i in cihazListesi:    # 2.yöntem
    #     f.write(i)
    f.seek(0)
    print(f.read())

#r+ mod ile açtım 2. bir with gerek yok
# with open("cihazlar.txt", encoding="utf-8") as f:
#     print(f.read())


#plain-text
#csv+json
#database