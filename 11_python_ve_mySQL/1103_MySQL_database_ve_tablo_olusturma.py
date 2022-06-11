# region mysql-baglan
# import mysql.connector
# connection = mysql.connector.connect(
#     host="localhost", 
#     user="root",
#     password="root",
#     database="firma"
# )
# cursor = connection.cursor()
# cursor.execute("show databases")
# for db in cursor:
#     print(db)
# endregion




import mysql.connector
connection = mysql.connector.connect(
    host="localhost", 
    user="root",
    password="root",
    database="firma"
)
cursor = connection.cursor()
sql ="""
    create table products(
        id int primary key auto_increment not null,
        product_name varchar(50) not null,
        description longtext not null,
        list_price decimal(19, 4) not null,
        category_id int not null
    );
"""
cursor.execute(sql)