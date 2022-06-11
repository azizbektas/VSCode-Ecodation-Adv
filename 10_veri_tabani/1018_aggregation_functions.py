# region agg_fun
"""
COUNT()	kaç adet var
MAX()	max değer
MIN()	min değer
SUM()	bir kolondaki toplam değerler
AVG()	bir kolondaki ortalama değerler




select
count(sicil)
from personel;

select
max(gelir)
from personel
where cinsiyet=1


select
min(gelir)
from personel
where cinsiyet=1

select
avg(gelir)
from personel;



select
sum(gelir)
from personel;




nested içi içe sorgu
select
*
from personel
where gelir = (
	select
	max(gelir)
	from personel
)

"""
# endregion
