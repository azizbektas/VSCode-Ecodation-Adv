# region personel_tablosu
"""
create table personel(
	sicil int not null,
    ad char(50) not null,
    soyad char(50) not null,
    dog_tar date,
    adres char(100),
    cinsiyet tinyint(1),
    gelir numeric(13, 2),
    bol_no smallint
);
"""
# endregion

# region urun_tablosu
"""
create table urun(
	urun_id int not null primary key,
    ad char(50) not null,
    satistaMi tinyint(1),
    tedarikci char(50) not null,
    kategori_id smallint
);
"""
# endregion

# region ogrenci_tablosu
"""
create table ogrenci(
	ogrenciNo int not null primary key,
    ad char(50) not null,
    soyad char(50) not null,
    tel char(15),
    adres char(200)
);
"""
# endregion

# region yonetici_tablosu
"""
create table yonetici(
	yonetici_id int primary key,
    ad_soyad varchar(25),
    ise_giris_tarihi date,
    mezuniyet varchar(25)
);
"""
# endregion

# region kimlik
"""
create table kimlik(
    ad char(50) not null,
    soyad char(50) not null,
    dog_tar date,
    sehir char(100)
);
"""
# endregion

# region stok_table
"""
create table stok(
	sNo int not null primary key,
    stokAdi varchar(50) not null,
    adet int ,
	fiyat real not null,
    sonKulTarihi date not null
);
"""
# endregion


# region alter_table
"""
/*var olan tabloya yeni kolon ekleme*/
alter table personel
add test_column varchar(50);


/*var olan tablodan kolon silme*/
alter table personel
drop test_column;
"""
# endregion

# region drop_table
"""
/*tüm tabloyu sil*/
drop table urun;
"""
# endregion



"""
create table ders(
	dersNo int not null primary key auto_increment,
    ders_ad char(50) not null,
    ders_kredi int not null
);
"""