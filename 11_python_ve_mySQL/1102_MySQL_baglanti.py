import mysql.connector
connection = mysql.connector.connect(
    host="localhost",  #burada IP yazarak harici DB e bağlanabiliriz
    user="root",
    password="root"
)
# print(connection)
if connection.is_connected():
    print("bağlandı")
else:
    print("bağlantı hatası")
