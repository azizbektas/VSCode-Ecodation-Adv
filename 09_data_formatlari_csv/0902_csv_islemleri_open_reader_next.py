# region csv_giris
'''
import csv
with open("xvericom-v1.csv", "r", encoding="utf-8") as csvFile:
    # print(csvFile.read())
    cReader = csv.reader(csvFile)
    # print(cReader)
    # print(type(cReader))
    # print(list(cReader))
    # print(list(cReader)[0])
    for row in cReader:
        # print(row[2]) # sadece email
        # print(f"ad soyad: {row[0]} {row[1]}")
        if row[4]=="İtalya":
            print(f"ad soyad: {row[0]} {row[1]}")
'''
# endregion
'''import csv
with open("devices.csv", "r", encoding="utf-8") as csvFile:
    cReader = csv.reader(csvFile)
    for row in cReader:
        # print(row)
        # print(row[0], row[2])
        if row[1]=="router":
            # print(row)
            print(f"device name: {row[0]} ip address: {row[2]} ")'''




import csv
with open("devices.csv", "r", encoding="utf-8") as csvFile:
    cReader = csv.reader(csvFile)
    next(cReader) #başlık olmadan okumak için
    for row in cReader:
        print(row)         