# region kargs_giris
"""
Argüman olarak → int, float, string, tuple, list gönderebiliyorum, peki
Argüman olarak → dictionary gönderebilir miyim? Cevabı, Evet
"""
# endregion





"""def pDilleri(**kargs):
    print(type(kargs))


pDilleri(
    programlamaDili="python",
    seviye = "yüksek",
    interpterer = True,
    version = 3.10
)"""





dilPython ={
    "programlamaDili" :"python",
    "seviye" : "yüksek",
    "interpterer" : True,
    "version" : 3.10
}


dilCSharp ={
    "programlamaDili" :"c#",
    "seviye" : "yüksek",
    "interpterer" : False,
    "version" : 8.0
}



def dilBilgisi(dil):
    # print(type(dil))
    print(f"{dil['programlamaDili']}\t\t{dil['seviye']}\t\t{dil['interpterer']}\t\t{dil['version']}")


print("Prg.Dili\tSeviye\t\tInterprt.\tVers.")
print("------\t\t-------\t\t-------\t\t------")
dilBilgisi(dilPython)
dilBilgisi(dilCSharp)