# region giris
#reader okuduk → python list olarak opere etti
#dictReader okuduk → python dictionary olarak opere edecek
'''from csv import DictReader #tüm modülü değilde sadece DictReader class'ı ekleyelim
with open("devices.csv", "r", encoding="utf-8") as csvFile:
    dReader = DictReader(csvFile)  
    # print(dReader)
    # print(type(dReader))
    for row in dReader:
        # print(row)
        if row["dType"]=="router":
            print(row)'''
# endregion

# CTRL + SHIFT + L
# bir dosyadaki tüm x karakterleri yerine y karakteri bas derken (vscode özelliği)
from csv import DictReader #tüm modülü değilde sadece DictReader class'ı ekleyelim
with open("devices.csv", "r", encoding="utf-8") as csvFile:
    dReader = DictReader(csvFile, delimiter=":")  
    # print(dReader)
    # print(type(dReader))
    for row in dReader:
        # print(row)
        if row["dType"]=="router":
            print(row)