# import mysql.connector
# connection = mysql.connector.connect(
#     host="localhost", 
#     user="root",
#     password="root",
#     database="firma"
# )
# cursor = connection.cursor()
# sql = "insert into products(product_name, description,list_price, category_id) values(%s, %s, %s, %s)"
# values=('iPhone 13', '128 GB', 21459.96, 2)
# cursor.execute(sql, values)
# try:
#     connection.commit()  # işlemek anlamına gelir
#     print(cursor.rowcount, "kayıt eklendi", "son kaydın id bilgisi", cursor.lastrowid)
# except mysql.connector.Error as e:
#     print("hata : ", e)
# finally:
#     connection.close()





#birden fazla kayıt ekleme
import mysql.connector
connection = mysql.connector.connect(
    host="localhost", 
    user="root",
    password="root",
    database="firma"
)
cursor = connection.cursor()
sql = "insert into products(product_name, description,list_price, category_id) values(%s, %s, %s, %s)"
values=[
    ('Vestel NF52101', 'No-Frost Buzdolabı', 6998.00, 3),
    ('Vestel CMI 97202 WIFI', '9 Kg 1000 Devir Çamaşır Makinesi', 5999.00, 3),
    ('Vestel SB14001', 'Mini Buzdolabı', 3339.00, 3),
]
cursor.executemany(sql, values)
try:
    connection.commit()  # işlemek anlamına gelir
    print(cursor.rowcount, "kayıt(lar) eklendi", "son kayıt(lar) id bilgisi", cursor.lastrowid)
except mysql.connector.Error as e:
    print("hata : ", e)
finally:
    connection.close()

