# file I/O
# region shell-pratikleri
"""
Type "help", "copyright", "credits" or "license" for more information.
>>> f = open("cihazlar.txt")
>>> f
<_io.TextIOWrapper name='cihazlar.txt' mode='r' encoding='cp1254'>
>>> f = open("cihazlar.txt", encoding="utf-8") 
>>> f
<_io.TextIOWrapper name='cihazlar.txt' mode='r' encoding='utf-8'>
>>> f.read()
'sw1,127.0.0.1'
>>>
"""
# endregion

# region split_hatirlama
"""
hatirlayalim = "A B C"
print(hatirlayalim.split())
hatirlayalim = "A,B,C"
print(hatirlayalim.split(","))
"""
# endregion 

# region giris
'''f = open("cihazlar.txt", encoding="utf-8")
# print(f.read())
result = f.read().split("\n")
# print(result)
for line in result:
    # print(line)
    if line[0:3]=="sw2":
        print(line[4:])'''
# endregion 

path = r"C:\Users\sensei\AppData\Local\PacketTracer\QtWebEngine"
f = open(f"{path}\kitaplar.txt", encoding="utf-8")
print(f.read())



#eğer dosya dizinde yok ise
import os
path = r"C:\Users\sensei\AppData\Local\PacketTracer\QtWebEngine"
files = os.listdir(path)
file = "kitaplarrrrr.txt"
# print(files)
if file not in files:
    print("böyle bir dosya yok")
else:
    f = open(f"{path}\{file}", encoding="utf-8")
    print(f.read())

'''f = open(f"{path}\kitaplarr.txt", encoding="utf-8")
print(f.read())'''