# region select_tum_tabloyu_okuma
"""
select
*
from stok;


select
*
from kimlik;


select
*
from personel;
"""
# endregion

# region select_sadece_belirli_kolonlari
"""
select
sicil, ad, soyad, dog_tar
from personel;
"""
# endregion

# region select_ilk_10_kayit
"""
select 
*
from personel;
"""
# endregion

# region select_sadece_belirli_kayit
"""
select 
*
from personel
where sicil=77;
"""
# endregion


# region select_query1
"""
select 
*
from personel
where sicil=77;


select 
*
from personel
where cinsiyet=1 and bol_no=43;
"""
# endregion


#kolon adına tr karakter basmak
"""
select
sicil, ad, soyad,dog_tar as 'doğum tarihi', adres, cinsiyet, gelir, fk_departman_id as 'bölüm id'
from personel;
"""