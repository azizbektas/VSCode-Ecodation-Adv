# region lab-pratigi-1-parola-politikası
""""
tr karakter girilmesin
min 8 karakter uzunluğunda olsun
"""
"""while True:
    trKarakterler = ["ş", "ç", "ğ", "ü", "ö", "ı", "İ"]
    p = input("parola politikası test et, çıkmak için [ç] : ")
    if p.lower() == "ç":
        break
    try:
        if len(p) < 8:
            raise Exception(
                "uygun olmayan parola - minimum karakter politikası")
        for i in p:
            if i in trKarakterler:
                raise Exception(
                    "uygun olmayan parola - tr karakter politikası")
        print("uygun parola")
    except Exception as e:
        print(e)"""
# endregion
