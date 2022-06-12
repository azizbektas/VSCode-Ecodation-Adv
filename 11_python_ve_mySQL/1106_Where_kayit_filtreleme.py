# import mysql.connector
# connection = mysql.connector.connect(
#     host="localhost", 
#     user="root",
#     password="root",
#     database="firma"
# )
# cursor = connection.cursor()
# sql = "select product_name, description, list_price from products where category_id=3"
# cursor.execute(sql)
# results = cursor.fetchall()  #retrive - fetchall → git al getir
# try:
#     print("Ürünler")
#     print("="*50)
#     print("Ürün Adı\t\tAçıklama\t\tFiyat")
#     for product in results:
#         print(f'{product[0]}\t {product[1]}\t\t\t ₺{product[2]:,.2f}')
#     print("="*50)
#     print(f"toplam {len(results)} kayıt görüntülendi")
# except mysql.connector.Error as e:
#     print("hata : ", e)
# finally:
#     connection.close()







#joker karakter → wildcard %

# import mysql.connector
# connection = mysql.connector.connect(
#     host="localhost", 
#     user="root",
#     password="root",
#     database="firma"
# )
# cursor = connection.cursor()
# sql = "select product_name, description, list_price from products where product_name like '%iphone%'"
# cursor.execute(sql)
# results = cursor.fetchall()  #retrive - fetchall → git al getir
# try:
#     print("Ürünler")
#     print("="*50)
#     print("Ürün Adı\tAçıklama\tFiyat")
#     for product in results:
#         print(f'{product[0]}\t{product[1]}\t\t₺{product[2]:,.2f}')
#     print("="*50)
#     print(f"toplam {len(results)} kayıt görüntülendi")
# except mysql.connector.Error as e:
#     print("hata : ", e)
# finally:
#     connection.close()




#sql injection hacker tekniği
import mysql.connector
connection = mysql.connector.connect(
    host="localhost", 
    user="root",
    password="root",
    database="firma"
)
cursor = connection.cursor()
sql = "select product_name, description, list_price from products where list_price>%s"
value = (15000,)
cursor.execute(sql,value)
results = cursor.fetchall()  #retrive - fetchall → git al getir
try:
    print("Ürünler")
    print("="*50)
    print("Ürün Adı\tAçıklama\tFiyat")
    for product in results:
        print(f'{product[0]}\t{product[1]}\t\t₺{product[2]:,.2f}')
    print("="*50)
    print(f"toplam {len(results)} kayıt görüntülendi")
except mysql.connector.Error as e:
    print("hata : ", e)
finally:
    connection.close()