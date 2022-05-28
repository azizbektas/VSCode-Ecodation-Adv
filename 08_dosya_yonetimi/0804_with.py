# region with_nedir
# f = open("cihazlar.txt", encoding="utf-8")
# print(f.read())
# f.close()

# kendim close demeden, tüm file i/o işlemlerinden sonra otomatik kapasın
# with open("cihazlar.txt", encoding="utf-8") as f:
#     print(f.read())
# print(f.closed)
# imdb_250.txt dosyasını nereden indirebilirim?
# bit.ly/aziz-hoca-paylas
# endregion


# region for_ile_search
# Forrest Gump top250 listesinde 6. sırada
'''try:
    with open("imdb_250.txt") as f:
        # print(f.read())
        i = 1
        fav= "Forrest Gump"
        for line in f.readlines():
            # print(f"{i}. {line}", end="")
            if line.strip("\n")==fav:
                print(f"{fav} top250 listesinde {i}. sırada")
            i += 1
except FileNotFoundError as e:
    print("dosya bulunamadı", e)'''
# endregion 



# region for_olmadan_search
# Forrest Gump top250 listesinde 6. sırada
try:
    with open("imdb_250.txt") as f:
        fav= "Forrest Gump\n"
        tumListe=f.readlines()
        # print(tumListe)
        if fav in tumListe:
            print(fav.rstrip('\n'), end=" ")
            print(f"top250 listesinde {tumListe.index(fav)+1} yer almamaktadır")
        else:
            print(fav.rstrip('\n'), end=" ")
            print("top250 listesinde yer almamaktadır")
except FileNotFoundError as e:
    print("dosya bulunamadı", e)
# endregion 