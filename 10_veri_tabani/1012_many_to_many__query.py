"""
/*1-many relation → ogrenci-ders-ogrenci_ders*/
create table ogrenci(
	ogrenciNo int not null primary key auto_increment,
    ad char(50) not null,
    soyad char(50) not null
);
alter table ogrenci auto_increment=100;




create table ders(
	dersNo int not null primary key auto_increment,
    ders_ad char(50) not null,
    ders_kredi int not null
);
alter table ders auto_increment=1000;



create table ogrenci_ders(
	ogrenci_ders_kod int auto_increment,
    ogrenci_no int,
    ders_kod int,
    vize int,
    final int,
    primary key(ogrenci_ders_kod, ogrenci_no, ders_kod),
    constraint fk_ogrDers
    foreign key (ogrenci_no) references ogrenci(ogrenciNo),
    foreign key (ders_kod) references ders(dersNo)
);
"""