"""
/*1-many relation → departman-departman city*/
create table departman(
	departman_id int primary key,
    ad varchar(25),
    butce numeric(13,2),
    lokasyon varchar(25)    
);


create table departman(
	sicil int not null,
    ad char(50) not null,
    soyad char(50) not null,
    dog_tar date,
    adres char(100),
    cinsiyet tinyint(1),
    gelir numeric(13, 2),
    fk_departman_id int not null,
    foreign key(fk_departman_id) references departman(departman_id)
);
"""