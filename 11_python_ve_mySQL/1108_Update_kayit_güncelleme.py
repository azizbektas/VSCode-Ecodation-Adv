# import mysql.connector
# connection = mysql.connector.connect(
#     host="localhost", 
#     user="root",
#     password="root",
#     database="firma"
# )
# cursor = connection.cursor()
# sql = "update products set product_name='çay' where id= 1"
# cursor.execute(sql)
# try:
#     rowCount=cursor.rowcount   # execute operasyonundan etkilenen kayıt sayısını geri döndürür
#     if rowCount>0:
#         result=input("güncellemek için e/E: ")
#         connection.commit()
#         print(rowCount, "kayıt(lar) güncellendi.")
# except mysql.connector.Error as e:
#     print("hata : ", e)
# finally:
#     connection.close()





#tamam ama yukarıdaki kod, hacker'ların sevdiği kod, sql injection önleyelim
import mysql.connector
connection = mysql.connector.connect(
    host="localhost", 
    user="root",
    password="root",
    database="firma"
)
cursor = connection.cursor()
sql = "update products set list_price=%s where id= %s"
values=(16000.95,3)
cursor.execute(sql, values)
try:
    rowCount=cursor.rowcount   # execute operasyonundan etkilenen kayıt sayısını geri döndürür
    if rowCount>0:
        result=input("güncellemek için e/E: ")
        connection.commit()
        print(rowCount, "kayıt(lar) güncellendi.")
except mysql.connector.Error as e:
    print("hata : ", e)
finally:
    connection.close()