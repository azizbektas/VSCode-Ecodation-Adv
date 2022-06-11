"""
#bölümler bazında grupladığımızda her bölümün ortalama gelir'i
select
bol_no, avg(gelir)
from personel
group by bol_no;

aynı zamanda order by yapabilirim
select
bol_no, avg(gelir)
from personel
group by bol_no
order by gelir;


çok çok çook değerli, peki select-from-orderby--- hangi sırada yazarız

select
*
from 
where 
group 
order by 

"""