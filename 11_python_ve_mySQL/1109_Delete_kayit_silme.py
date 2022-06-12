# import mysql.connector
# connection = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="root",
#     database="firma"
# )
# cursor = connection.cursor()
# sql = "delete from products where id=5"
# cursor.execute(sql)
# try:
#     connection.commit()
#     print(cursor.rowcount, "kayıt(lar) silindi.")
# except mysql.connector.Error as e:
#     print("hata : ", e)
# finally:
#     connection.close()




# kullanıcı onayı
import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="firma"
)
cursor = connection.cursor()
# idToDelete=int(input("Silinecek Id: "))
# sql = "delete from products where id=%s"
sql = "delete from products"
# values=(idToDelete,)
# cursor.execute(sql, values)
cursor.execute(sql)
try:
    rowCount=cursor.rowcount   # execute operasyonundan etkilenen kayıt sayısını geri döndürür
    if rowCount>0:
        result=input("silmek için e/E: ")
        connection.commit()
        print(rowCount, "kayıt(lar) silindi.")
except mysql.connector.Error as e:
    print("hata : ", e)
finally:
    connection.close()