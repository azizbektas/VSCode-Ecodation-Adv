"""
/*inner join*/
select 
ad, ders_ad, vize, final
from ogrenci, ders, ogrenci_ders
where ogrenci.ogrenciNo=ogrenci_ders.ogrenci_no and ders.dersNo=ogrenci_ders.ders_kod
"""