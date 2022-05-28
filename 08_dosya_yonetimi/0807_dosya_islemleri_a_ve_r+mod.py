# region dosya_acma_modlari
"""
Dosya Açma Modları	→  	[ r ] 	:   read-okuma 
					                dosya çağırılan dizinde değil ise hata verir
                        [ x ] 	:   oluşturma 
					                oluşturulan dosya adı çağırılan dizinde mevcut ise hata verir
				        [ w ] 	:   write-yazma,
                                    dosya çağırılan dizinde oluşturulur, 
                                    eğer konumda aynı dosyadan var ise,
                                    dosya içeriğini siler ve yeniden yazma operasyonu yapar
				        [ a ] 	:   append-ekleme
                                    dosya çağırılan dizinde yoksa oluşturulur, 
                                    son satıra ekleme operasyonu yapar,
                                    seek metodu ile birlikte kullanılamaz		
				        [ r+ ] 	:   read/write-okuma/yazma
                                    dosya çağırılan dizinde değil ise hata verir,
                                    ilk satıra ekleme operasyonu yapar,
                                    seek metodu ile birlikte kullanılabilir
"""
# endregion