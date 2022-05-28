# region giris
'''f = open("cihazlar.txt", encoding="utf-8")
# print(type(f.readline()))
# print(f.readline(), end="")
# print(f.readline(), end="")
# print(f.readline(), end="")



# print(f.readlines())
lines = f.readlines()
# print(lines[0], end="")
# print(lines[1], end="")
for line in lines:
    #\n başa bela, hem readlines dan geliyor hem print ten
    #çözüm 1
    # print(line, end="")
    #çözüm 1
    print(line.rstrip("\n"))'''
# endregion

f = None
try:
    path = r"C:\Users\sensei\AppData\Local\PacketTracer\QtWebEngine"
    f = open(f"{path}\kitaplarr.txt", encoding="utf-8")
    print(f.read())
except FileNotFoundError:
    print("Dosya Bulunamadı")
finally:
    if f is not None:
        f.close()
