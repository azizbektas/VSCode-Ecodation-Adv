# import mysql.connector
# connection = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="root",
#     database="firma"
# )
# cursor = connection.cursor()
# sql = "select * from products limit 2"
# cursor.execute(sql)
# results=cursor.fetchall()
# try:
#     for product in results:
#         print(product)
# except mysql.connector.Error as e:
#     print("hata : ", e)
# finally:
#     connection.close()



# 5 kayıt ötele, ondan sonraki 5 kaydı getir

import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="firma"
)
cursor = connection.cursor()
sql = "select * from products limit 5 offset 5"
cursor.execute(sql)
results=cursor.fetchall()
try:
    for product in results:
        print(product)
except mysql.connector.Error as e:
    print("hata : ", e)
finally:
    connection.close()