# import mysql.connector
# connection = mysql.connector.connect(
#     host="localhost", 
#     user="root",
#     password="root",
#     database="firma"
# )
# cursor = connection.cursor()
# # sql = "select product_name, description, list_price from products order by product_name desc"
# sql = "select product_name, description, list_price from products order by list_price desc"
# cursor.execute(sql)
# results = cursor.fetchall()
# try:
#     for product in results:
#         print(f'{product[0]}\t{product[1]}\t\t₺{product[2]:,.2f}')
#         # print(product)
# except mysql.connector.Error as e:
#     print("hata : ", e)
# finally:
#     connection.close()




#kullanıcıdan alalım
import mysql.connector
connection = mysql.connector.connect(
    host="localhost", 
    user="root",
    password="root",
    database="firma"
)
cursor = connection.cursor()
# sql = "select product_name, description, list_price from products order by product_name desc"
ynt = int(input("lütfen sıralama kriterine yanıt verin artan[1] - azalan[0] : "))
if ynt==1:
    sql = "select product_name, description, list_price from products order by list_price asc"
else:
    sql = "select product_name, description, list_price from products order by list_price desc"
cursor.execute(sql)
results = cursor.fetchall()
try:
    for product in results:
        print(f'{product[0]}\t{product[1]}\t\t₺{product[2]:,.2f}')
        # print(product)
except mysql.connector.Error as e:
    print("hata : ", e)
finally:
    connection.close()