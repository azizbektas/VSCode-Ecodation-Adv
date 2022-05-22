# region syntax_error
"""aylar = {
    "ocak":31,
    "şubat":28
    "mart":31
}"""
# endregion

# region name_error
"""aylar = {
    "ocak":31,
    "şubat":28,
    "mart":31
}
print(ay["ocak"])"""
# endregion

# region key_error
"""aylar = {
    "ocak":31,
    "şubat":28,
    "mart":31
}
print(aylar["nisan"])"""
# endregion

# region index_error
"""aylar = [
    "ocak",
    "şubat",
    "mart"
]
print(aylar[3])"""
# endregion

# region type_error
"""
a = "python"
b = 4
c = "networker"
print(a+b+c)
x = "python4networker"
# print(x.count(4))
print(x.count("4"))
"""
# endregion

# region attribute_error
"""
x = "python4networker"
print(x.Count("4"))
"""
# endregion

# region value_error
"""
a = int(input("Sayı : "))
print(10/a) # a→iki girildiğinde
"""
# endregion

# region ZeroDivisionError_error
"""
a = int(input("Sayı : "))
print(10/a) # a→0 girildiğinde
"""
# endregion


# shell script anında tüm hataları görmek için
# >>> import builtins
# >>> dir(builtins)