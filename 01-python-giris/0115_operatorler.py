# region aritmetik-operatorler
# aritmetik operatörler
"""
1→  +   toplama
2→  -   çıkarma
3→  *   çarpma
4→  /   bölme
5→  //  tam bölme
6→  **  üst alma
7→  %   mod alma
"""
# endregion

# region + -
"""
print(4+4)
print(4+14)
print(4-14)
print(-5.0 + 15)
print(-5. + 15)
result = type(-5. + 15)
print(result)
# unary → sayıların işareti
print(-9)
print(+9)
"""
# endregion

# region * /
"""
print(3*3)
a = 15
# shift + alt + f → formatter

print(10/0)
"""
# endregion

# region **
"""
print(3**3)
print(3**3.)
print(16**.5)
print(16**0.5)
print(16**(1/2))
"""

# endregion

# region //
"""
print(12/7)
print(12//7)
print(12//7.)
print(12/5)
print(12//5)
print(12/5)
print(12//5)
print(-13/5)
print(-13//5)
"""
# endregion

# region %
"""
print(15 % 4)
print(12 % 4.5)
print(12 % 0)
print(type(12 % 4.5))
"""

# endregion

# region operator_oncelikleri
"""
1→  +, -        unary
2→  **          üst alma
3→  *, /, %     çarpma, bölme, mod alma
4→  +,-         toplama çıkarma
"""
"""
print(3+4*5)
print(15%4*2)   #% left-side binding
print(15%4%2)   #% left-side binding
print(2**2**3)  #** right-side binding
"""
# endregion