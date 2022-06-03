# region giris
'''from csv import reader, writer
#import csv de olur
# with open("orders.csv") as csvFile:
#     cReader = reader(csvFile)
#     for row in cReader:
#         print(row)
with open("new-orders.csv", "w", newline="") as csvFile:
    cWriter = writer(csvFile)
    cWriter.writerow(["CustomerId","ShipCountry"])
    cWriter.writerow(["BrkGunal","Konya"])
    cWriter.writerows([["xCustomer","xCountry"], ["yCustomer","yCountry"]])'''
# endregion

#region header-data
'''from csv import reader, writer
header = [
    "CustomerId",
    "ShipCountry"
]
data = [
    ["BrkGunal","Konya"],
    ["xCustomer","xCountry"],
    ["yCustomer","yCountry"]
]
with open("new-orders.csv", "w", newline="") as csvFile:
    cWriter = writer(csvFile)
    cWriter.writerow(header)
    cWriter.writerows(data)'''
# endregion


# reigon orderdan_oku_new_ordera_yaz
from csv import reader, writer
with open("orders.csv") as csvFile:
    cReader = reader(csvFile)
    with open("new-orders.csv", "w", newline="") as csvFile:
        cWriter = writer(csvFile)
        for row in cReader:
            if row[2]=="False":
                cWriter.writerow(row)
# endregion
