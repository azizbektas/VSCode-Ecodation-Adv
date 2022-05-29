# region dosya_acma_modlari
"""
Dosya Açma Modları	→  	[ r ] 	:   read-okuma,
					                dosya çağırılan dizinde değil ise hata verir
                        [ x ] 	:   oluşturma,
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



# w modunun kötü tarafı aynı isimde var ise, önceki verileri siler 
'''with open("cihazlar.txt", "w", encoding="utf-8") as f:
    # print(f)
    f.write("1→switch")'''








'''with open("cihazlar.txt", "a", encoding="utf-8") as f:
    f.write("7→umbrella\n")'''



# append mod açında, üzgünüm seek metodu çalışmaz, cursor'u istediğin yere taşıyazmazsın
'''with open("cihazlar.txt", "a", encoding="utf-8") as f:
    f.seek(0)
    f.write("1→nexus\n")'''



with open("cihazlar.txt", "r+", encoding="utf-8") as f:
    f.read()
    f.write("9→switch\n")