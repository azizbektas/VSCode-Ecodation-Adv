"""
/*1-1 relation → counrty-capital city*/

create table country(
	country_id int primary key,
    name varchar(25)
);

#cccId → capital city country id
create table capital_city(
	city_id int primary key,
    city_name varchar(25),
    cccId int references country(country_id),
    constraint fk_country_cccId unique(cccId)
);
"""





"""
/*1-1 relation → yonetici-bolum*/
create table yonetici(
	yonetici_id int primary key,
    ad_soyad varchar(25),
    ise_giris_tarihi date,
    mezuniyet varchar(25)
);

create table bolum(
	bolum_id int primary key,
    ad varchar(25),
    butce numeric(13, 2),
    lokasyon varchar(25),
    yonetici_id int references yonetici(yonetici_id),
    constraint fk_yonetici_yonetici_id unique(yonetici_id)
);
"""


