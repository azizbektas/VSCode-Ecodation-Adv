# import mysql.connector
# connection = mysql.connector.connect(
#     host="localhost", 
#     user="root",
#     password="root",
#     database="firma"
# )
# cursor = connection.cursor()
# sql = """
#     select * 
#     from products
# """
# cursor.execute(sql)
# results = cursor.fetchall()  #retrive - fetchall → git al getir
# try:
#     # print(type(results))
#     for product in results:
#         print(product)
# except mysql.connector.Error as e:
#     print("hata : ", e)
# finally:
#     connection.close()





#sadece belirli kolonlar
# import mysql.connector
# connection = mysql.connector.connect(
#     host="localhost", 
#     user="root",
#     password="root",
#     database="firma"
# )
# cursor = connection.cursor()
# sql = """
#     select product_name, description, list_price 
#     from products
# """
# cursor.execute(sql)
# results = cursor.fetchall()  #retrive - fetchall → git al getir
# try:
#     # print(type(results))
#     for product in results:
#         # print(product)
#         print(product[0], product[1], f"₺{product[2]:,.2f}")
# except mysql.connector.Error as e:
#     print("hata : ", e)
# finally:
#     connection.close()








#sadece belirli kolonlar ve sadece tek bir kaydı → fetchone
import mysql.connector
connection = mysql.connector.connect(
    host="localhost", 
    user="root",
    password="root",
    database="firma"
)
cursor = connection.cursor()
sql = """
    select product_name, description, list_price 
    from products
"""
cursor.execute(sql)
product = cursor.fetchone()  #retrive - fetchall → git al getir
try:
    print(product[0], product[1], f"₺{product[2]:,.2f}")
except mysql.connector.Error as e:
    print("hata : ", e)
finally:
    connection.close()