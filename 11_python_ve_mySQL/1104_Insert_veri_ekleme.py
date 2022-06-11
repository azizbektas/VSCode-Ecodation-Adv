import mysql.connector
connection = mysql.connector.connect(
    host="localhost", 
    user="root",
    password="root",
    database="firma"
)
cursor = connection.cursor()
sql = "insert into products(product_name, description,list_price, category_id) values(%s, %s, %s, %s)"
values=('iPhone 13', '128 GB', 21459.96, 2)
cursor.execute(sql, values)
try:
    connection.commit()  # işlemek anlamına gelir
    print(cursor.rowcount, "kayıt eklendi", "son kaydın id bilgisi", cursor.lastrowid)
except mysql.connector.Error as e:
    print("hata : ", e)
finally:
    connection.close()

