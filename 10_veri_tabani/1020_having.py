#orderby kullanıldığında filtreleme için having kullanırız
"""
select
bol_no, gelir, ad
from personel
where cinsiyet= 1
group by bol_no
having gelir>6000
"""