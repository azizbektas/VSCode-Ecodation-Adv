# region scope_kapsam_giris
"""
1→ python main fonksiyon ile yani main kısmı ile fonksiyon arasında değişken aktarımları, 
2→ main deki değişkeni fonksiyon görebilecek mi değiştirebilecek mi? 
3→ fonksiyondaki değişkene main kısmından erişim yapabilecek miyim?
4→ fonksiyondaki değişkenin içeriğini değiştirdiğimde, maindeki de değişecek mi? 
"""
# endregion


"""def scopeTest():
    a = 34


scopeTest()
print(a)"""


"""
def scopeTest():
    a = 34
    print(id(a))

a = 19
scopeTest()
print(id(a))
"""


"""
def scopeTest():
    print(id(a))

a = 19
scopeTest()
print(id(a))
"""


"""def scopeTest():
    global a
    a = 34
    print(a)

a = 19
scopeTest()
print(a)"""


"""def scopeTest(a): 
    print(a) #19    
    a += 1
    print(a) # 20

a = 19
scopeTest(a)
print(a) #19"""


def scopeTest(arg):
    print(arg)
    # arg = [19, 34, 35]
    del arg[0]


liste = [19, 34]
scopeTest(liste)
print(liste)
