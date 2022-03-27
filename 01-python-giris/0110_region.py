# region uygulama
def kartBilgiVer(k):
    return f"{k['ad']} {k['soyad']} {k['bankaAdi']} {k['para']}"
def atmBilgiVer(a):
    return f"{a['ad']} {a['para']}"
def ayniMi(k, a):
    if k['bankaAdi'] == a['ad']:
        return True
    else: 
        return False
def paraYatir(k, a, miktar):
    k['para'] += miktar
    a['para'] += miktar
    if not ayniMi(k, a):
        k['para'] -= miktar*0.03
        a['para'] += miktar*0.03
    print(f"{miktar} para yatırıldı. ATM'de {a['para']} TL. oldu")
def paraCek(k, a, miktar):
    if a['para']>=miktar:
        if k['para']>=miktar:
            k['para'] -= miktar
            a['para'] -= miktar
            if not ayniMi(k, a):
                k['para'] -= miktar*0.03
                a['para'] += miktar*0.03
                print(f"kartınızdan {miktar*0.03} TL. ücret alındı")
            print(f"{miktar} TL. Çekildi. Atm'de {a['para']} kaldı. Hesabınızda da {k['para']} kaldı.")
        else:
            print(f"Bakiyenizde bu kadar para yok. En fazla {k['para']} TL. çekebilirsiniz")
    else:
        print(f"ATM'de Bu KAdar PAra Yok {a['para']} miktar çekebilirsiniz...")
kart = {
    "ad": "ali",
    "soyad" : "kemal",
    "bankaAdi": "zirat",
    "para": 100
}
atm = {
    "ad":"halk",
    "para":350
}
print(kartBilgiVer(kart))
print(atmBilgiVer(atm))
paraYatir(kart, atm, 100)
print("-"*50)
print(kartBilgiVer(kart))
print(atmBilgiVer(atm))
paraCek(kart, atm, 50)
print("-"*50)
print(kartBilgiVer(kart))
print(atmBilgiVer(atm))

# endregion 

# region db-baglan

# endregion








# region ilk-app

# endregion





"""
♥   alt + 3
→   alt + 26
Dünya'nın♥En♥Güzel♥Şehri→İstanbul
"""


