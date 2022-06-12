def infoDb():
    import mysql.connector
    connection = mysql.connector.connect(
        host="localhost", 
        user="root",
        password="root",
        database="firma"
    )
    return connection

def createEmp():
    connection=infoDb()
    cursor = connection.cursor()
    sql = """
        create table employees(
            id int primary key auto_increment, 
            name varchar(50) not null,
            surname varchar(50) not null,
            address varchar(150) not null,
            gender tinyint(1) not null,
            department_id int not null
        );
    """
    cursor.execute(sql)

def insertEmp(name, surname, address, gender, department_id):
    connection=infoDb()
    cursor=connection.cursor()
    sql="insert into employees(name, surname, address, gender, department_id) values(%s, %s, %s, %s, %s)"
    values=(name, surname,address, gender, department_id)
    cursor.execute(sql, values)
    try:
        connection.commit()
        print(cursor.rowcount, "kayıt(lar) eklendi")
    except Exception as e:
        print("hata: ", e)
    finally:
        connection.close()

def insertEmps(list):
    connection=infoDb()
    cursor= connection.cursor()
    sql="insert into employees(name, surname, address, gender, department_id) values(%s, %s, %s, %s, %s)"
    values=(list)
    cursor.executemany(sql, values)
    try:
        connection.commit()
        print(cursor.rowcount, "kayıt(lar) eklendi")
    except Exception as e:
        print("hata: ", e)
    finally:
        connection.close()

def getEmps():
    connection=infoDb()
    cursor=connection.cursor()
    sql ="""
        select *
        from employees
    """
    cursor.execute(sql)
    results=cursor.fetchall()
    try:
        for employee in results:
            if employee[4]==1:
                print(f"id: {employee[0]}, ad: {employee[1]}, soyad: {employee[2]}, adres: {employee[3]}, cinsiyet: erkek, bölüm: {employee[5]}")
            else:
                print(f"id: {employee[0]}, ad: {employee[1]}, soyad: {employee[2]}, adres: {employee[3]}, cinsiyet: kadın, bölüm: {employee[5]}")
    except Exception as e:
        print("hata : ", e)
    finally:
        connection.close()

def getEmpById(id):
    connection=infoDb()
    cursor=connection.cursor()
    sql ="select * from employees where id=%s"
    values=(id, )
    cursor.execute(sql, values)
    result=cursor.fetchall()
    try:
        if result[0][4]==1:
            print(f"id: {result[0][0]}, ad: {result[0][1]}, soyad: {result[0][2]}, adres: {result[0][3]}, cinsiyet: erkek, bölüm: {result[0][5]}")
        else:
            print(f"id: {result[0][0]}, ad: {result[0][1]}, soyad: {result[0][2]}, adres: {result[0][3]}, cinsiyet: kadın, bölüm: {result[0][5]}")
    except Exception as e:
        print("hata : ", e)
    finally:
        connection.close()

def deleteById(id):
    connection= infoDb()
    cursor=connection.cursor()
    sql="delete from employees where id=%s"
    values=(id, )
    cursor.execute(sql, values)
    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt(lar) silindi")
    except Exception as e:
        print("hata : ", e)
    finally:
        connection.close()

def updateById(id, address):
    connection=infoDb()
    cursor=connection.cursor()
    sql="update employees set address=%s where id=%s"
    values=(address, id)
    cursor.execute(sql, values)
    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt(lar) güncellendi")
    except Exception as e:
        print("hata : ", e)
    finally:
        connection.close()



# region main
msg = "-----\n[1] - Çalışan Tablosu Oluştur\n[2] - Çalışan Ekle\n[3] - Çalışanlar Ekle\n[4] - Tüm Kaydı Listele\n[5] - Id'e Göre Listele\n[6] - Id'e Göre Sil\n[7] - Id'e Göre Güncelle\n[8] - Çık"
calisanListe=[]
while True:
    print(msg)
    islem = input("Seçim : ")
    if islem=="8":
        break
    elif islem=="1":
        createEmp()
    elif islem=="2":
        name = input("Ad Giriniz: ")
        surname = input("Soyad Giriniz: ")
        address = input("Adres Giriniz: ")
        gender = input("Cinsiyet [0/1] Giriniz: ")
        department = input("Departman:  ")
        insertEmp(name, surname, address, gender, department)
        getEmps()
    elif islem=="3":
        while True:
            name = input("Ad Giriniz: ")
            surname = input("Soyad Giriniz: ")
            address = input("Adres Giriniz: ")
            gender = input("Cinsiyet [0/1] Giriniz: ")
            department = input("Departman:  ")
            calisanListe.append((name, surname, address, gender, department))
            result= input("ekleme işlemine devam mı e/h: ")
            if result.lower()=="h":
                insertEmps(calisanListe)
                break
    elif islem=="4":
        getEmps()
    elif islem=="5":
        getEmps()
        secim = input("lütfen listelenecek çalışan id giriniz: ")
        getEmpById(secim)
    elif islem=="6":
        getEmps()
        secim = input("lütfen silinecek çalışan id giriniz: ")
        deleteById(secim)
    elif islem=="7":
        getEmps()
        secim = input("lütfen güncellenenecek çalışan id giriniz: ")
        yeniAdres = input("Yeni Adres Bilgisi: ")
        updateById(secim, yeniAdres)
        getEmps()
    else:
        print("hatalı seçim")
# endregion
